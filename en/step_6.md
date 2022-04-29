## Find matching coordinates

Now that the features that are the same on each image have been matched, the coordinates of those features need to be fetched.

--- task ---

Create a new function that takes the two sets of keypoints as arguments.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 50
line_highlights: 50
---
def find_matching_coordinates(keypoints_1, keypoints2):
--- /code ---

--- /task ---

--- task ---

Create two empty lists, to store the coordinates of each matching feature, in each of the images.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 50
line_highlights: 51-52
---
def find_matching_coordinates(keypoints_1, keypoints2):
    coordinates_1 = []
    coordinates_2 = []
--- /code ---

--- /task ---

The list of matches contains many OpenCV `match` objects. You can iterate through the list, to find the coordinates of each match on each image.

--- task ---

Add a `for` loop to fetch the coordinates (`x1`, `y1`, `x2`, `y2`) of each match.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 50
line_highlights: 53-57
---
def find_matching_coordinates(keypoints_1, keypoints2):
    coordinates_1 = []
    coordinates_2 = []
    for match in matches
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1,y1) = keypoints_1[image_1_idx].pt
        (x2,y2) = keypoints_2[image_2_idx].pt
--- /code ---

--- /task ---

--- task ---

Then those coordinates can be added to the two coordinates lists, and the two lists can be returned.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 50
line_highlights: 58-60
---
def find_matching_coordinates(keypoints_1, keypoints2):
    coordinates_1 = []
    coordinates_2 = []
    for match in matches
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1,y1) = keypoints_1[image_1_idx].pt
        (x2,y2) = keypoints_2[image_2_idx].pt
        coordinates_1.append((x1,y1))
        coordinates_2.append((x2,y2))
    return coordinates_1, coordinates_2
--- /code ---

--- /task ---

--- task ---

Add a function call to the bottom of you script to store the outputs of the function

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 63
line_highlights: 68
---
time_difference = get_time_difference(image_1, image_2) #get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors
display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches) #display matches
coordinates_1, coordinates_2 = find_matching_coordinates(keypoints_1, keypoints_2, matches)
--- /code ---

--- /task ---

--- save ---