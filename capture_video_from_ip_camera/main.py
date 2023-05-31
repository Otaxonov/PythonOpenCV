import cv2
import os

RTSP_URL = 'rtsp://username:password@192.168.1.110:554/Streaming/channels/201/'

# Use tcp instead of udp if stream is unstable
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

stream = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not stream.isOpened():
    print("Cannot open RTSP stream")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = stream.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv2.imshow('RTSP stream', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
stream.release()
cv2.destroyAllWindows()
