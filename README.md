# Stop Sign Detection with Simulated UART or Arduino Control

This project detects stop signs in real-time using a webcam and OpenCV, and simulates or sends UART signals to control a robot (e.g., via Arduino).

---

## System Overview

- Uses a **Haar Cascade Classifier** to detect stop signs from a **live webcam feed**
- Sends a `1` over UART for **3 seconds** when a stop sign is detected
- Then resumes sending `0` continuously
- UART output is:
  - **Simulated in console** (default)
  - **Can be enabled to communicate with Arduino** via Serial

---

## Folder Structure

