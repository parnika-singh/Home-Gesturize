import cv2 as cv
import os

path = r'C:\Users\dell\Desktop\faltu\photo\Camera'      # r: for taking raw
# test_path = 'C:\Users\dell\Desktop\faltu\photo\Camera'
os.chdir(path)     #to change the directory
os.getcwd()         #to get current working diorectory
video_file = r'20190608_122932.mp4'

cap = cv.VideoCapture(video_file)
#cap for "Video Capture Object"
if not cap.isOpened():
    print("Error opening Video File.")
try:
    while True:
        
    # Capturing frame-by-frame
        ret, frame = cap.read()       #ret: return value that is bool value(true/false)
    
        cv.imshow('frames',frame)
        if cv.waitKey(5) & 0xFF == ord('q'):
            break

    # if frame is read correctly, ret is True
        elif not ret:        #if not true
            print("Can't retrieve frame - stream may have ended. Exiting..")
            break
except:    #assertion error coming 
    print("Video has ended.")
#everything done, releasing the capture
cap.release()
cv.destroyAllWindows()
