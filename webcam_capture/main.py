import cv2

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = webcam.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('webcam', gray)
    
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
webcam.release()
cv2.destroyAllWindows()
