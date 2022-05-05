## Display matching features

Matches can be displayed on both images, with lines linking each of the matched keypoints.

--- task ---

Delete the final `print` call at the end of your script.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 42
line_highlights: 46
---
time_difference = get_time_difference(image_1, image_2) #get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors

--- /code ---

--- /task ---


--- task ---

Crate a function, below your other functions, that takes the two OpenCV image objects, the keypoints and the matches as arguments.

--- code ---
---
language: python
filename: calc_speed.cv
line_numbers: true
line_number_start: 42
line_highlights: 42
---
def display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches):


time_difference = get_time_difference(image_1, image_2) #get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors
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
filename: iss_speed.py
line_numbers: false
line_number_start: 
line_highlights: 5
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

--- save ---