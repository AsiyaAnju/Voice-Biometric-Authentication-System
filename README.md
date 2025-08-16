# Voice Biometric Authentication System
![Voice Auth](https://img.shields.io/badge/Biometric-VoiceAuth-green?logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)

Voice Biometric Authentication System focuses on verifying user identity through unique vocal characteristics instead of traditional passwords or PINs. It leverages Deep learning algorithms, and anti-spoofing mechanisms to provide a secure, seamless, and efficient authentication method. The system analyzes distinct vocal features such as tone, pitch, frequency, and speech patterns to create a voiceprint for each user. This approach enhances security, convenience, and accessibility, making it ideal for applications in banking, IoT devices, smart home systems, enterprise security, and hands-free authentication scenarios.

## Overview 

* The Voice Biometric Authentication System is a real-time speaker verification framework that enhances security using machine learning-based voice recognition. 
* It extracts unique voice features using MFCCs and applies preprocessing techniques like noise suppression and pre-emphasis filtering for improved clarity. 
* The system employs Euclidean distance-based matching with a dynamic threshold to minimize false acceptances and rejections, and uses CNN-based speaker recognition for accurate spectrogram-based classification. 
* The backend is Python-based, enabling secure and efficient voice authentication. 
* Extensive testing under various conditions confirms high accuracy and robustness, making the system suitable for applications like banking, IoT, and access control. 

## Features

1. *Voice Recording* – captures voice samples using sounddevice
2. *Local Storage* – saves recordings and user voiceprints in voiceprints.pkl
3. *Feature Extraction* – extracts MFCC features with librosa for unique voice patterns
4. *Noise Reduction* – applies background noise suppression using noisereduce
5. *Similarity Check* – compares voices using Euclidean distance for authentication
6. *Voice Guidance* – provides step-by-step assistance using pyttsx3 text-to-speech

## Tech Stack
1. *Programming Language*: <img src="https://cdn.simpleicons.org/python/3776AB" height="15em" alt="Python" />&nbsp;Python

2. *Audio Processing*:
<br>librosa – feature extraction (MFCCs, pre-emphasis)
<br>noisereduce – background noise reduction
<br>sounddevice – voice recording
<br>wavio – saving audio files
3.*Machine Learning Approach*:
<br>Feature-based comparison using Euclidean Distance
4. *Voice Assistance*:
<br>pyttsx3 – text-to-speech guidance
5. *Data Handling*:
<br>pickle – storing user voiceprints
<br>numpy – numerical computations
6. *Environment*: Local execution (no cloud/server needed)

# Requirement Analysis
## Hardware Requirements
1. High-Quality Microphone – Captures clear voice samples with minimal noise; noise-canceling recommended.
2. Processing Unit (CPU/GPU) – Multi-core processor (Intel i5/i7, AMD Ryzen 5/7+); GPU (NVIDIA RTX/GTX) for deep learning.
3. RAM (Memory) – Minimum 8GB (16GB+ recommended) for efficient AI model processing.
4. Storage (SSD Preferred) – At least 256GB SSD; 1TB+ for large voiceprint databases.
5. Audio Processing Hardware (Optional) – DSPs for real-time noise filtering and voice enhancement.

## Software Requirements
1. Operating System: Windows 10/11, macOS, or Linux (Ubuntu preferred)
2. Programming Language: Python 3.7 or above
3. Required Libraries: numpy, librosa, sounddevice, wavio, pyttsx3, noisereduce, pickle
4. Development Tools : VS Code / PyCharm and pip / conda for package management
5. Audio Support: Microphone access enabled, 22050 Hz sample rate
6. Storage: Local file handling for .wav files & voiceprints.pkl

# 📂 Project Structure
<img width="840" height="202" alt="image" src="https://github.com/user-attachments/assets/96f19840-5bd0-4ea2-9000-edbdcb947543" />

## 📚 Documentation
- 📑 Project Report => Voice Biometric Authentication System - Report
- 📊 Project Presentation => Voice Biometric Authentication System - Presentation

# Installation and Set-up
1. Clone the Repository
<br>&nbsp;&nbsp;git clone https://github.com/AsiyaAnju/Voice-Biometric-Authentication-System.git
<br>&nbsp;&nbsp;cd Voice-Biometric-Authentication-System

2. Install Dependencies
<br>&nbsp;&nbsp;pip install -r requirements.txt

3. Run the Script
<br>&nbsp;&nbsp;python main.py

4. Setup Authentication (First Time)
* Enter a username
* Speak 3 times to register your voice
* Your averaged voiceprint will be saved

5. Verify Authentication
* Enter your username again
* Speak once
* System checks similarity with stored voiceprint

<br>➡️ Important:
<br>Works best in a quiet environment
<br>Accuracy may drop with background noise
<br>Threshold can be adjusted in code (similarity < 25)
<br>Currently stores data locally only (no server/database)

# System Design and Architecture
1️⃣ User Voice Acquisition<br>
2️⃣ Feature Extraction<br>
3️⃣ Deep Learning-Based Authentication<br>
4️⃣ Security & Encryption<br>
5️⃣ User Verification & Decision Making<br>
<p align="center"><img width="350" height="500" alt="image (3)" src="https://github.com/user-attachments/assets/9365bb2b-c818-4434-9d3d-73012ff6e215" /></p>

# Methodology
<p align="center">
<img width="500" height="800" alt="image (2)" src="https://github.com/user-attachments/assets/7c3dd04e-0fbb-421e-96ef-eba44de028cc" />
</p>

## Future Improvements

1. Use ML models (e.g., SVM, neural networks) to improve the authentication model and achieve better accuracy.
2. Add GUI for easier interaction.
3. Store encrypted voiceprints in a secure database.
4. Allow multiple users with management
5. Enhance security

## 👤 Author
- Asiya Anjum S
- GitHub: AsiyaAnju
- LinkedIn: https://www.linkedin.com/in/asiyaanjums

