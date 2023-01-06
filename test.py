import cv2

#Capture video from webcam
vid_capture = cv2.VideoCapture('rtsp://admin:Admin@12345@192.168.0.250:554/cam/realmonitor?channel=1&subtype=0')
vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("videos/cam_video.mp4", vid_cod, 20.0, (1280 ,720))

while(True):
     # Capture each frame of webcam video
     ret,frame = vid_capture.read()
     cv2.imshow("My cam video", frame)
     output.write(frame)
     # Close and break the loop after pressing "x" key
     if cv2.waitKey(1) &0XFF == ord('x'):
         break

# close the already opened camera
vid_capture.release()
# close the already opened file
output.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()