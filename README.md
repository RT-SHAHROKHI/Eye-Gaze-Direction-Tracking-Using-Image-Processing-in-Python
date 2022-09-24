# Eye-and-gaze-tracking-with-image-processing
Python code for eye and gaze tracking

First of all we import the libraries: Opencv and numpy.
0 in "cap = cv2.VideoCapture()" is for opening the camera and then we put it in a loop so tha we can loop through the frames of the video and process image by image.

  import cv2
  import numpy as np

  cap = cv2.VideoCapture(0)

  while True:
      ret, frame = cap.read()
      if ret is False:
          break
        
then we select an Roi (region of interest).
In this way we are restricting the detection only to the pupil, iris and sclera and cutting out all the unnecessary things like eyelashes and the area surrounding the eye.        

  roi = frame[269: 795, 537: 1416]
  rows, cols, _ = roi.shape
  gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)


Our focus is on the pupil. By converting the image into grayscale format we will see that the pupil is always darker then the rest of the eye. No matter where the eye is looking at and no matter what color is the sclera of the person.
To do so, first conversion to grayscale and then we find the threshold to extract only the pupil.

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

    _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV)
    
From the threshold we find the contours. And we simply remove all the noise selecting the element with the biggest area (which is supposed to be the pupil) and skip all the rest.
    
     contours, hierachy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        cv2.line(frame, (x + int(w/2), 0), (x + int(w/2), rows), (0, 0, 0), 2)
        cv2.line(frame, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 0, 0), 2)
        break
        
        
Finally we show everything on the screen.


    cv2.imshow("Threshold", threshold)
    #cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", frame)
    key = cv2.waitKey(30)
    if key == 27:
        break
    cv2.destroyAllWindows()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
