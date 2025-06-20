import cv2
import time

# === Optional: Uncomment below if using Arduino via Serial ===
# import serial
# ser = serial.Serial('COM3', 9600, timeout=1)  # Replace 'COM3' with your actual port

# === Load Haar Cascade ===
stop_cascade = cv2.CascadeClassifier('stop_sign_classifier.xml')

# === Initialize Camera ===
cap = cv2.VideoCapture(0)

# === Control Flags ===
sending_stop = False
stop_start_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect stop signs
    stops = stop_cascade.detectMultiScale(gray, 1.3, 5)

    if len(stops) > 0 and not sending_stop:
        print("[INFO] Stop sign detected!")
        sending_stop = True
        stop_start_time = time.time()

    # Handle UART signal sending
    if sending_stop:
        print("Sending: 1")  # Simulated UART
        # ser.write(b'1\n')  # Uncomment when using Arduino
        if time.time() - stop_start_time > 3:
            sending_stop = False
    else:
        print("Sending: 0")  # Simulated UART
        # ser.write(b'0\n')  # Uncomment when using Arduino

    # Draw rectangles around detected stop signs
    for (x, y, w, h) in stops:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show the camera feed
    cv2.imshow('Stop Sign Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# === Close Serial Port if used ===
# ser.close()