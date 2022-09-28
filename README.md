Python code for eye and gaze tracking

How to use : 
make sure that your eye is visible on the screen when you run the code to see proper output.

Download exe file of the code :
https://drive.google.com/file/d/1_5ZI3jwP6APg4gOV-ZVxZZtV9pRhkE5a/view?usp=sharing

About the code : 
After opening the camera, we create a loop through the frames of the video and begin our process image by image.
We select a Roi (region of interest). In this way we are restricting the detection only to the eye and cutting out all the unnecessary things.
Our focus is on the pupil. By converting the image into grayscale format we will see that the pupil is always darker then the rest of the eye.
To do so, first conversion to grayscale and then we find the threshold to extract only the pupil.
From the threshold we find the contours. And we simply remove all the noise selecting the element with the biggest area (which is supposed to be the pupil) and skip all the rest.
Finally we show everything on the screen.

