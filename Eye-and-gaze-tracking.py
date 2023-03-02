import cv2

def limit_the_Size(frame):
   return frame[269: 795, 400: 1416]

def convert_to_gray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def blur(roi):
    return cv2.GaussianBlur(roi, (7, 7), 0) 

def threshold_inv(roi):
    return cv2.threshold(roi, 3, 255, cv2.THRESH_BINARY_INV)

def find_boundaries(threshold):
    return cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def Choose_pupil_boundaries(contours):
    return sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True) 

def draw_rectangle(contours, frame, color, size ):
        for cnt in contours:
            (x, y, weight, height) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + weight, y + height), color, size)        # draw the white rectangle around the pupil
            break

def draw_vertical_line(contours, frame, color, size ):
        for cnt in contours:
            (x, y, weight, height) = cv2.boundingRect(cnt)
            cv2.line(frame, (x + int(weight/2), 0), (x + int(weight/2), rows), color, size) # draw the vertical line passing through the middle of the pupil 
            break

def draw_horizontal_line(contours, frame, color, size ):
        for cnt in contours:
            (x, y, weight, height) = cv2.boundingRect(cnt)
            cv2.line(frame, (0, y + int(height/2)), (cols, y + int(height/2)), color, size) # draw the horizontal line passing through the middle of the pupil
            break

def ShowOutput(frame):
    return cv2.imshow("Roi", frame)   
#----------------------------------------------------------------------------
white = (255, 255, 255)
black = (0, 0, 0) 
size_of_the_line = 2 
size_of_the_rectangle = 2
#----------------------------------------------------------------------------

# main : 

webcam_URL = "https://192.168.1.100:8080/video"

# cap = cv2.VideoCapture(0) #Open system camera
cap = cv.2VideoCapture(webcam_URL) #Open IP camera as webcam

while True:

    ret, frame = cap.read() #to read input frames from the camera 
    if ret is False:
        break

    frame              = limit_the_Size(frame) # to limit the input window as short as possible to see only an eye & nothing more
    rows, cols, _      = frame.shape
    roi                = convert_to_gray(frame) # for using thersholding and detect pupil which is pure black 
    roi                = blur(roi) # to reduce noise
    _, threshold       = threshold_inv(roi) # with using threshold(BINARY_INV) ; pupil which is always darker then the rest of the eye turns into white but almost evrything else (evrything brighter than pupil) is going to be black 
    contours, hierachy = find_boundaries(threshold) 
    contours           = Choose_pupil_boundaries(contours)
    
    draw_rectangle      (contours, frame, white, size_of_the_rectangle) # draw the white rectangle around the pupil
    draw_vertical_line  (contours, frame, black, size_of_the_line     ) # draw the vertical line passing through the middle of the pupil
    draw_horizontal_line(contours, frame, black, size_of_the_line     ) # draw the horizontal line passing through the middle of the pupil
    ShowOutput(frame) # the output window showing : 1-real-time input which an eye can be seen in it 2-rectangle around the pupil & 2 lines passing through the middle of it
    
    key = cv2.waitKey(30) # wait 30 ms before going to the next frame and process it
    if key == 27:
        break
cv2.destroyAllWindows()
