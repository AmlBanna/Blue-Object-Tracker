import cv2
import numpy as np

cap = cv2.VideoCapture(0)

  
blue_lower = np.array([100, 50, 50])
blue_upper = np.array([140, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   
    mask = cv2.inRange(hsv, blue_lower, blue_upper)

    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    cv2.imshow('Object Tracking', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
