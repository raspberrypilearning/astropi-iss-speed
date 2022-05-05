## Find matching features

The next step is to find matching features on the two images. There are algorithms to do this in OpenCV.

--- task ---

Delete the `print` statement from your code.

--- code ---
---
language: python
filename: iss_speed.py
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
filename: iss_speed.py
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

Delete your call to `print(get_time_difference('photo_07464.jpg', 'photo_07465.jpg')` on line 22.

--- /task ---

--- task ---

To process images they need to be converted to OpenCV objects, so add a function that takes the two images as arguments and then returns those objects.

--- code ---
---
language: python
filename: iss_speed.py
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
filename: iss_speed.py
line_numbers: true
line_number_start: 28
line_highlights: 28-33
---
def calculate_features(image_1, image_2, feature_number):
    orb = cv2.ORB_create(nfeatures = feature_number)
    keypoints_1, descriptors_1 = orb.detectAndCompute(image_1_cv, None)
    keypoints_2, descriptors_2 = orb.detectAndCompute(image_2_cv, None)
    return keypoints_1, keypoints_2, descriptors_1, descriptors_2
--- /code ---

--- /task ---

Now you have the keypoints and descriptors of the keypoints, they need to be matched between the two images. This will tell you whether a keypoint in the first image is the same keypoint in the second image. The simplest way to do this is to use brute force.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">**Brute force**</span> algorithm means the computer is trying every possible combination. It's like trying to unlock a pin protected phone by starting with the pin `0000`, then moving on to `0001` and keep going until it unlocks or you get to `9999`.
</p>

**Brute force**, in this context, means that you take a descriptor from the first image and try to match it against **all** the descriptors in the second image. A match will either be found or not. Then you take the second descriptor from the first image and repeat the process, and then repeat it again until you have compared every descriptor in the first image and compared it to the ones second.

--- task ---

Write a function that takes the two sets of descriptors and tries to find matches by brute force.

--- code ---
---
language: python
filename: iss_speed.py
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

Now that you have your matches, you can run all your functions and have a look at the output.

--- task ---

Assign the two images you want to use, and add function calls to the end of your script to run your functions and print out the matches.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start:42
line_highlights: 
---
image_1 = 'photo_07464.jpg'
image_2 = 'photo_07465.jpg'


time_difference = get_time_difference(image_1, image_2) #get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors
print(matches)
--- /code ---

--- /task ---

The result should look something like this:

```
[<DMatch 0F73B548>, <DMatch 0F73B4A0>, <DMatch 0F73C560>, <DMatch 0F719E60>...
```

This is a list of matches along with the keypoint. It's not very helpful though, so in the next step you can plot the matches on the images and view them.

--- save ---