# Real-Time Emotion AI Assistant

A real-time AI-powered assistant that detects human emotions from facial expressions using computer vision and provides voice feedback. This project combines face detection, deep learning-based emotion analysis, and text-to-speech interaction in a simple and interactive system.

---

## Features

* Real-time face detection using OpenCV
* Emotion recognition using DeepFace
* Voice feedback using text-to-speech (pyttsx3)
* Interactive control using keyboard input
* Lightweight and easy to run locally

---

## How It Works

1. The system captures live video from the webcam.
2. Faces are detected using Haar Cascade Classifier.
3. When the user presses **'S'**, the system starts scanning.
4. A short delay allows stable detection.
5. DeepFace analyzes the face and detects the dominant emotion.
6. The result is displayed on screen and spoken aloud.

---

##  Technologies Used

* Python
* OpenCV
* DeepFace
* pyttsx3
* NumPy

---

##  Controls

* Press **S** → Start emotion scanning
* Press **Q** → Quit the application



This project is developed for learning and demonstrating real-time AI and computer vision concepts.
