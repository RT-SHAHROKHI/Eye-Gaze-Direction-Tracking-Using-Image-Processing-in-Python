Bachelor's final project: Eye Gaze Direction Tracking Using Image Processing in Python

How to use : 
Run the code and make sure that your eye is visible on the screen when you run the code to see proper output.

Download exe file of the code :
https://drive.google.com/file/d/1_5ZI3jwP6APg4gOV-ZVxZZtV9pRhkE5a/view?usp=sharing

Download outputs of tests subjects' video:
https://drive.google.com/file/d/1zNZx0piZTH7mnlfKo7gfg8hnKZDrJIFl/view?usp=sharing

About the code : 
After opening the camera, we create a loop through the frames and start our processing image by image.
We select a Roi (region of interest). In this way we are restricting the detection to the eye only and remove all unnecessary things.
Our focus is on the pupil. By converting the image to grayscale format, we will see that the pupil is always darker than the rest of the eye.
Therefore, after convert the image to grayscale it is time to apply thresholding to extract only the pupil.
From the threshold, we find the contours. And we simply remove all noise by selecting the element with the largest area (which is supposed to be the pupil) and ignore the rest. Finally, we display everything on the screen.
