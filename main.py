import numpy as np
import librosa
import sounddevice as sd
import wavio
import pickle
import os
import pyttsx3
import noisereduce as nr  # Noise reduction library

#print("Script started")

# Constants
SAMPLE_RATE = 22050
DURATION = 5  # Increased duration for better sample quality
VOICE_DB = "voiceprints.pkl"
SAVE_DIR = "voice_recordings"

# Ensure save directory exists
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Capture voice sample
def record_voice(file_name):
    full_path = os.path.join(SAVE_DIR, file_name)
    speak("Recording... Please speak clearly.")
    audio = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    wavio.write(full_path, audio, SAMPLE_RATE, sampwidth=2)
    speak(f"Recording saved to {full_path}.")
    return full_path

# Apply noise reduction
def denoise_audio(y, sr):
    y_denoised = nr.reduce_noise(y=y, sr=sr, stationary=True)
    return y_denoised

# Extract features with noise suppression
def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=SAMPLE_RATE)
    y = denoise_audio(y, sr)  # Remove background noise
    y = librosa.effects.preemphasis(y)  # Enhances clarity of voice
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

# Load or initialize voice database
if os.path.exists(VOICE_DB):
    with open(VOICE_DB, "rb") as f:
        voiceprints = pickle.load(f)
else:
    voiceprints = {}

# Setup voice authentication with noise-free samples
def setup_voice(user_id):
    speak(f"Setting up voice authentication for {user_id}. Please speak multiple times.")
    samples = []
    
    for i in range(3):  # Collect multiple voice samples for accuracy
        speak(f"Sample {i+1}: Please speak now.")
        file_path = record_voice(f"{user_id}_{i}.wav")
        features = extract_features(file_path)
        if features is not None:
            samples.append(features)

    if samples:
        voiceprints[user_id] = np.mean(samples, axis=0)  # Store averaged features
        with open(VOICE_DB, "wb") as f:
            pickle.dump(voiceprints, f)
        speak("Voice authentication setup complete.")
    else:
        speak("Setup failed due to noise issues. Please try again in a quieter environment.")

# Verify user voice with flexible threshold
def verify_voice(user_id):
    if user_id not in voiceprints:
        speak("No registered voice found. Setting up authentication.")
        setup_voice(user_id)
        return
    
    speak("Speak to verify your identity.")
    file_path = record_voice("test.wav")
    features = extract_features(file_path)
    
    if features is None:
        speak("Verification failed due to noise. Please try again in a quieter environment.")
        return
    
    similarity = np.linalg.norm(features - voiceprints[user_id])
    
    if similarity < 25:  # Increased threshold for better tolerance
        speak("Authentication successful!")
        print("✅ Authentication successful!")
    else:
        speak("Authentication unsuccessful!,please try again")
        print("❌ Authentication unsuccessful!")

# Main execution

print("Waiting for username input...")
user_name = input("Enter your username: ")
print(f"Username entered: {user_name}")

verify_voice(user_name)