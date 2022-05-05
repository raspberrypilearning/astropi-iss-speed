## Calculate average speed

Now that the feature distances have been calculated for the two photographs, this needs converting to how far apart the features actually are on Earth. Once that has been calculated the time difference between the two photos can be used to calculate the speed of the camera, and therefore the speed of the ISS.

--- task ---

Delete your print call at the bottom of your script.

--- /task ---

--- task ---

Create a new function to calculate the speed of the ISS. It should take the `feature_distance`, a `GSD` factor and the `time_difference` as arguments.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 74
line_highlights: 74
---
def calculate_speed_in_kmps(feature_distance, GSD, time_difference):
--- /code ---

--- /task ---

You can use [this website](https://www.3dflow.net/ground-sampling-distance-calculator/) to calculate the scaling factor between distance in pixels and distance on Earth. The ground sample distance (GSD) is given in centimeters/pixels. You need the distance in kilometers though, and there are 100000 centimeters in a kilometer.

--- task ---

Calculate the distance by multiplying the feature distance in pixels by the `GSD` and then divide it all by 100000

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 74
line_highlights: 75
---
def calculate_speed_in_kmps(feature_distance, GSD, time_difference):
    distance = feature_distance * GSD / 100000
--- /code ---

--- /task ---

--- task ---

The speed can then be calculated by dividing by the `time_difference` between the two images, and the speed returned.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 74
line_highlights: 76-77
---
def calculate_speed_in_kmps(feature_distance, GSD, time_difference):
    distance = feature_distance * GSD / 100000
    speed = distance / time_difference
    return speed
--- /code ---

--- /task ---

[The Ground Sampling Distance](https://www.3dflow.net/ground-sampling-distance-calculator){:target='_blank'} site gives a `GDS` of 12648 for the HQ Camera on the ISS.

--- task ---

Call your function and then print the result at the end of your program.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: false
line_number_start:
line_highlights: 7-8
---
time_difference = get_time_difference(image_1, image_2) #get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors
display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches) #display matches
coordinates_1, coordinates_2 = find_matching_coordinates(keypoints_1, keypoints_2, matches)
average_feature_distance = calculate_mean_distance(coordinates_1, coordinates_2)
speed = calculate_speed_in_kmps(average_feature_distance, 12648, time_difference)
print(speed)
--- /code ---

--- /task ---

With the two images used in this project, a value of `7.255443210895204` is returned, which is not far from the 7.66 kmps speed that the ISS actually travels at.

--- save ---
