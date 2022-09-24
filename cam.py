import cv2 as cv
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    frame = frame[269: 795, 400: 1416]
    rows, cols, _ = frame.shape
    gray_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

    _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV)
    contours, hierachy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        cv2.line(frame, (x + int(w/2), 0), (x + int(w/2), rows), (0, 0, 0), 2)
        cv2.line(frame, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 0, 0), 2)
        break

    cv2.imshow("Threshold", threshold)
    #cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", frame)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()



