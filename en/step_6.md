## Find matching coordinates

Now that the features that are the same on each image have been matched, the coordinates of those features need to be fetched.

--- task ---

Create a new function that takes the two sets of keypoints and the list of matches as arguments.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 54
line_highlights: 54
---
def find_matching_coordinates(keypoints_1, keypoints_2, matches):
--- /code ---

--- /task ---

--- task ---

Create two empty lists to store the coordinates of each matching feature in each of the images.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 54
line_highlights: 55-56
---
def find_matching_coordinates(keypoints_1, keypoints_2, matches):
    coordinates_1 = []
    coordinates_2 = []
--- /code ---

--- /task ---

The list of matches contains many OpenCV `match` objects. You can iterate through the list to find the coordinates of each match on each image.

--- task ---

Add a `for` loop to fetch the coordinates (`x1`, `y1`, `x2`, `y2`) of each match.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 54
line_highlights: 57-58
---
def find_matching_coordinates(keypoints_1, keypoints_2, matches):
    coordinates_1 = []
    coordinates_2 = []
    for match in matches:
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1,y1) = keypoints_1[image_1_idx].pt
        (x2,y2) = keypoints_2[image_2_idx].pt
--- /code ---

--- /task ---

--- task ---

Next, those coordinates can be added to the two coordinates lists, and the two lists can be returned.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 54
line_highlights: 62-64
---
def find_matching_coordinates(keypoints_1, keypoints_2, matches):
    coordinates_1 = []
    coordinates_2 = []
    for match in matches:
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

Add a function call to the bottom of you script to store the outputs of the function.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: false
line_number_start: 67
line_highlights: 72
---
time_difference = get_time_difference(image_1, image_2) # Get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) # Create OpenCV image objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) # Get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) # Match descriptors
display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches) # Display matches
coordinates_1, coordinates_2 = find_matching_coordinates(keypoints_1, keypoints_2, matches)
--- /code ---

--- /task ---

--- save ---
