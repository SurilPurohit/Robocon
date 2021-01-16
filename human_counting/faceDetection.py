import cv2 # library used to develop real time computer vision(image processing, video capture, face detection etc)

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml') # # initialize front face classifier
cap = cv2.VideoCapture(0) # start capturing using webcam where 0 indicates number of the camera
cap.set(3,640) # set Width of screen 
cap.set(4,480) # set Height of screen

while True:
    ret, img = cap.read() # returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of the video by checking this return value.
    img = cv2.flip(img, 1) # used to flip the screen where 1 stands for vertical image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converts an image from one color space to another. Here we are Converting to black-and-white
    
    faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, # Parameter specifying how much the image size is reduced at each image scale.
        minNeighbors=5, # Parameter specifying how many neighbors each candidate rectangle should have to retain it.
        minSize=(20, 20), # Minimum possible object size. Objects smaller than that are ignored.
    ) 
    

    for (x,y,w,h) in faces: # coordinates of the detected face
        cv2.rectangle( # draw rectangle around detected face 
            img, # Window name in which image is displayed
            (x,y), # represents the top left corner of rectangle
            (x+w,y+h), # represents the bottom right corner of rectangle
            (255,0,0), # Blue color in BGR
            2) # Line thickness of 2 px
        roi_gray = gray[y:y+h, x:x+w] # location of the face
        roi_color = img[y:y+h, x:x+w] # location of the face
        face_no = faces.shape[0]; #assigning nnumbers to faces
        cv2.putText(img, str(face_no), (x, y - 30), cv2.FONT_HERSHEY_TRIPLEX,
                .7, (0, 0, 0), 1, cv2.LINE_AA) #printing numbers of the faces just above the rectangle
        
        
    # Display the webcam
    cv2.imshow('video',img)

    # press 'ESC' to quit/stop webcam
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
