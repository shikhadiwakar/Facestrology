import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Use the Haar Cascade Classifier to detect eyes in the live video stream
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Counter for naming the saved images
counter = 0

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    
    # Detect eyes in the frame
    eyes = eye_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    
    # Iterate over the eyes detected and crop each eye region
    for (x,y,w,h) in eyes:
        # Crop the eye region from the original frame
        eye_img = frame[y:y+h, x:x+w]
        # Display the cropped eye region
        cv2.imshow('Eye', eye_img)
        # Save the cropped eye region to disk
        cv2.imwrite(f'eye_{counter}.jpg', eye_img)
        counter += 1
    
    # Display the live video stream
    cv2.imshow('Live Video', frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
