## Find matching features

The next step is to find matching features on the two images. There are algorithms to do this in OpenCV.

--- task ---

Delete the `print` statement from your code.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 13
line_highlights: 20
---
def get_time_difference(image_1, image_2):
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    time_difference = time_2 - time_1
    return time_difference.seconds



--- /code ---

--- /task ---

--- task ---

Install the `opencv-python` package in Thonny

--- /task ---

[[[thonny-install-package]]]

--- task ---

Import the `cv2` package and the inbuilt `math` package at the top of your script.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 
line_highlights: 3-4
---
from exif import Image
from datetime import datetime
import cv2
import math
--- /code ---

--- /task ---

--- task ---

To process images they need to be converted to OpenCV objects, so add a function that takes the two images as arguments and then returns those objects.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 22
line_highlights: 22-25
---
def convert_to_cv(image_1, image_2):
    image_1_cv = cv2.imread(image_1, 0)
    image_2_cv = cv2.imread(image_2, 0)
    return image_1_cv, image_2_cv
--- /code ---

--- /task ---

The OpenCV objects that have been returned can now be used by other classes and methods in the OpenCV package. For this project the Oriented FAST and Rotated BRIEF (ORB) algorithm can be used. This algorithm will detect **Keypoints** in an image or in several images. If the images are similar, then the same keypoints in each image should be detected, even if some features have moved or changed. ORB can also assign **Descriptors** to the keypoints. These will contain information on how the keypoint, such as its position, size, rotation and brightness. By comparing the descriptors between keypoints, the changes from one image to the other can be calculated.

--- task ---

Write a function to find the keypoints and descriptors for the two images. It will take three arguments. The first two are the OpenCV image objects and the last is the maximum number of features you want to search for.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 28
line_highlights: 28-33
---
def calculate_features(image_1, image_2, feature_number):
    orb = cv2.ORB_create(nfeatures = feature_number)
    keypoints_1, descriptors_1 = orb.detectAndCompute(image_1_cv, None)
    keypoints_2, descriptors_2 = orb.detectAndCompute(image_2_cv, None)
    return keypoints_1, key_points2, descriptors_1, descriptors_2
--- /code ---

--- /task ---

Now you have the keypoints and descriptors of the keypoints, they need to be matched between the two images. This will tell you whether a keypoint in the first image is the same keypoint in the second image. The simplest way to do this is to use brute force.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">**Brute force**</span> algorithms mean the computer is trying every possible combination. It's like trying to unlock a pin protected phone by starting with the pin `0000`, then moving on to `0001` and keep going until it unlocks or you get to `9999`.
</p>

Brute force, in this context, means that you take a descriptor from the first image and try to match it against **all** the descriptors in the second image. A match will either be found or not. Then you take the second descriptor from the first image and repeat the process, and then repeat it again until you have compared every descriptor in the first image and compared it to the ones second.

--- task ---

Write a function that takes the two sets of descriptors and tries to find matches by brute force.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 35
line_highlights: 35-39
---
def calculate_matches(descriptors_1, descriptors_2):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(descriptors_1, descriptors_2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches
--- /code ---

--- /task ---

Now that you have the matches, you can display them on the two images, side by side. This will let you visualise what the algorithm you have written is doing.

--- task ---

Crate a function that takes the two OpenCV image objects, the keypoints and the matches as arguments.

--- code ---
---
language: python
filename: calc_speed.cv
line_numbers: true
line_number_start: 42
line_highlights: 42
---
def display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches):
--- /code ---

--- /task ---

--- task ---

Next draw lines between the keypoints where the descriptors match.

--- code ---
---
language: python
filename: calc_speed.cv
line_numbers: true
line_number_start: 42
line_highlights: 43
---
def display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches):
    match_img = cv2.drawMatches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches[:100], None)
--- /code ---

--- /task ---

--- task ---

The images can now be resized and shown, side by side on your screen, with the lines drawn between the matches.

--- code ---
---
language: python
filename: calc_speed.cv
line_numbers: true
line_number_start: 42
line_highlights: 44-45
---
def display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches):
    match_img = cv2.drawMatches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches[:100], None)
    resize = cv2.resize(match_img, (1600,600), interpolation = cv2.INTER_AREA)
    cv2.imshow('matches', resize)

--- /code ---

--- /task ---

--- task ---

To finish off the function, the script needs to wait until a key is pressed, and then close the image.

--- code ---
---
language: python
filename: calc_speed.cv
line_numbers: true
line_number_start: 42
line_highlights: 44-45
---
def display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches):
    match_img = cv2.drawMatches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches[:100], None)
    resize = cv2.resize(match_img, (1600,600), interpolation = cv2.INTER_AREA)
    cv2.imshow('matches', resize)
    cv2.waitKey(0)
    cv2.destroyWindow('matches')
--- /code ---

--- /task ---

--- task ---

All these functions now need to be called in order, so that you can see the output.

At the bottom of you script add the following lines:

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 48
line_highlights: 48-52
---
time_difference = get_time_difference(image_1, image_2) #get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors
display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches) #display matches
--- /code ---

--- /task ---

--- task ---

Run your code and you should see an image like the one below. Click in the window and press any key to exit the image view.

![side by side of images of the Earth, with similar features on each image having lines drawn between them](images/matches.png)

--- /task ---
