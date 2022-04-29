from exif import Image
from datetime import datetime
import cv2
import math


def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    return time
    
    
def get_time_difference(image_1, image_2):
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    time_difference = time_2 - time_1
    return time_difference.seconds


def convert_to_cv(image_1, image_2):
    image_1_cv = cv2.imread(image_1, 0)
    image_2_cv = cv2.imread(image_2, 0)
    return image_1_cv, image_2_cv


def calculate_features(image_1, image_2, feature_number):
    orb = cv2.ORB_create(nfeatures = feature_number)
    keypoints_1, descriptors_1 = orb.detectAndCompute(image_1_cv, None)
    keypoints_2, descriptors_2 = orb.detectAndCompute(image_2_cv, None)
    return keypoints_1, keypoints_2, descriptors_1, descriptors_2


def calculate_matches(descriptors_1, descriptors_2):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(descriptors_1, descriptors_2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches
    

def display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches):
    match_img = cv2.drawMatches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches[:100], None)
    resize = cv2.resize(match_img, (1600,600), interpolation = cv2.INTER_AREA)
    cv2.imshow('matches', resize)
    cv2.waitKey(0)
    cv2.destroyWindow('matches')
    
    
def find_matching_coordinates(keypoints_1, keypoints2):
    list_keypoints_1 = []
    list_keypoints_2 = []
    for match in matches:
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1,y1) = keypoints_1[image_1_idx].pt
        (x2,y2) = keypoints_2[image_2_idx].pt
        list_keypoints_1.append((x1,y1))
        list_keypoints_2.append((x2,y2))
    return list_keypoints_1, list_keypoints_2


def calculate_mean_distance(list_kp1, list_kp2):
    average_distance = 0
    number_matches = len(matches)

    for c in range(number_matches):
        distance = math.hypot(list_kp1[c][0] - list_kp2[c][0], list_kp1[c][1] - list_kp2[c][1])
        average_distance = average_distance + distance
    return average_distance / number_matches
    

def calculate_speed_in_kmps(feature_distance, scaling, time_difference):
    metre_distance = feature_distance * (scaling / 100)
    speed = metre_distance / time_difference
    kmps = speed / 1000
    return kmps


image_1 = 'photo_07464.jpg'
image_2 = 'photo_07465.jpg'


time_difference = get_time_difference(image_1, image_2) #get time difference between images
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors
print(matches)
display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches) #display matches
list_keypoints_1, list_keypoints_2 = find_matching_coordinates(keypoints_1, keypoints_2)
average_feature_distance = calculate_mean_distance(list_keypoints_1, list_keypoints_2)
speed = calculate_speed_in_kmps(average_feature_distance, 12648, time_difference)
print(speed)