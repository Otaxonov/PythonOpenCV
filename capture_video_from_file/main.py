import cv2

video = cv2.VideoCapture("Python in 100 Seconds.mp4")

while video.isOpened():
    # Capture frame-by-frame
    ret, frame = video.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()
