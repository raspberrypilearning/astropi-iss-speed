## Calculate feature distance

With the coordinates of matching features stored, the distance between the coordinates of the matching features can be calculated. This will be the distance on the images though, so it will need to be converted to the equivalent kilometer distance on Earth, and then divided by the time difference between the photos, to calculate the speed.

--- task ---

Create a function to calculate the average distance between matching coordinates. Call it `calculate_mean_distance` that takes two arguments, which will be the two coordinates lists.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 63
line_highlights: 63
---
def calculate_mean_distance(coordinates_1, coordinates_2):
--- /code ---

--- /task ---

The Python `zip` function will take items from two lists and join them together. So the 0th item from the first list and the 0th item from the second list are combined together. Then the 1st items from each of the lists are combined together. The zipped lists can easily be converted back to a single simple list.

--- task ---

Start by creating a variable to store the total of all the distances between coordinates and call it `all_distances`. Then you can `zip` the two lists and then convert the zipped object back to a list.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 63
line_highlights: 64-65
---
def calculate_mean_distance(coordinates_1, coordinates_2):
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2))
--- /code ---

--- /task ---

To see what has happened here, you can add some `print` calls to see the details of the lists.

--- task ---

Add three `print` calls to see an item in `coordinates_1`, `coordinates_2` and `merged_coordinates`.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 63
line_highlights: 66-68
---
def calculate_mean_distance(coordinates_1, coordinates_2):
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2))
    print(coordinates_1[0])
    print(coordinates_2[0])
    print(merged_coordinates[0])
--- /code ---

--- /task ---

--- task ---

Add a call to your function at the bottom of your script.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 
line_highlights: 
---
average_feature_distance = calculate_mean_distance(coordinates_1, coordinates_2)
--- /code ---

When you run the code, you should see output that looks like this:
```
(3002.400146484375, 1620.0001220703125)
(3428.64013671875, 1637.280029296875)
((3002.400146484375, 1620.0001220703125), (3428.64013671875, 1637.280029296875))
```

--- /task ---

Hopefully you can see that the `x` and `y` coordinate from each feature, from each image, have been combined. This will allow for easy iteration over the new list.

--- task ---

Delete the `print` calls and add a `for` loop to iterate over the `merged_coordinates` and calculate the differences between the `x` and `y` coordinates in each image.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 63
line_highlights: 66-68
---
def calculate_mean_distance(coordinates_1, coordinates_2):
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2))
    for coordinate in merged_coordinates:
        x_difference = coordinate[0][0] - coordinate[1][0]
        y_difference = coordinate[0][1] - coordinate[1][1]
--- /code ---

--- /task ---

Look at the following image

![Triangle with points A, B, C and lengths a, b, c](images/triangle.png)

The distance between points **A** and **B** is the length of the line **c**. This is called the hypotenuse. Using the `math` package, the hypotenuse (`hypot`) can be calculated.

--- task ---

Calculate the distance between the two points and add them to the `all_distances` variable.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 63
line_highlights: 69-70
---
def calculate_mean_distance(coordinates_1, coordinates_2):
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2))
    for coordinate in merged_coordinates:
        x_difference = coordinate[0][0] - coordinate[1][0]
        y_difference = coordinate[0][1] - coordinate[1][1]
        distance = math.hypot(x_difference, y_difference)
        all_distances = all_distance + distances
--- /code ---

--- /task ---

--- task ---

Return the average distance between the features, by dividing `all_distances` by the number of feature matches, which is the length of the `merged_coordinates` list.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: true
line_number_start: 63
line_highlights: 71
---
def calculate_mean_distance(coordinates_1, coordinates_2):
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2))
    for coordinate in merged_coordinates:
        x_difference = coordinate[0][0] - coordinate[1][0]
        y_difference = coordinate[0][1] - coordinate[1][1]
        distance = math.hypot(x_difference, y_difference)
        all_distances = all_distance + distances
    return all_distances / len(merged_coordinates)
--- /code ---

--- /task ---

--- task ---

Add a function call at the bottom of your code to calculate the average distance, and then print the result.

--- code ---
---
language: python
filename: calc_speed.py
line_numbers: false
line_number_start: 78
line_highlights: 84-85
---
time_difference = get_time_difference(image_1, image_2) #get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors
display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches) #display matches
coordinates_1, coordinates_2 = find_matching_coordinates(keypoints_1, keypoints_2, matches)
average_feature_distance = calculate_mean_distance(coordinates_1, coordinates_2)
print(average_feature_distance)
--- /code ---

--- /task ---

When you run your code you should get an answer like `516.2791658606644`

--- save ---
