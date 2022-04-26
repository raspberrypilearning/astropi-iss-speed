import cv2
import math
from exif import Image
from datetime import datetime


def get_time(image):
    with open(image, 'rb') as image_file:
        frame = Image(image_file)
        #print(frame1.datetime)
        time = datetime.strptime(frame.datetime, '%Y:%m:%d %H:%M:%S')
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


def calculate_features(image_1, image_2):
    orb = cv2.ORB_create(nfeatures=500)
    key_points_1, description_1 = orb.detectAndCompute(image_1_cv, None)
    key_points_2, description_2 = orb.detectAndCompute(image_2_cv, None)
    return key_points_1, key_points_2, description_1, description_2


def calculate_matches(description_1, description_2):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(description_1, description_2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches
    
    
def find_matching_coordinates(key_points_1, key_points2):
    list_key_points_1 = []
    list_key_points_2 = []
    for match in matches:
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1,y1) = key_points_1[image_1_idx].pt
        (x2,y2) = key_points_2[image_2_idx].pt
        list_key_points_1.append((x1,y1))
        list_key_points_2.append((x2,y2))
    return list_key_points_1, list_key_points_2


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


def display_matches(image_1_cv, key_points_1, image_2_cv, key_points_2, matches):
    match_img = cv2.drawMatches(image_1_cv, key_points_1, image_2_cv, key_points_2, matches[:100], None)
    rs = cv2.resize(match_img, (1600,600), interpolation = cv2.INTER_AREA)
    cv2.imshow('m', rs)
    cv2.waitKey(0)
    cv2.destroyWindow('m')


image_1 = 'cv2comp2/photo_07464.jpg'
image_2 = 'cv2comp2/photo_07465.jpg'


time_difference = get_time_difference(image_1, image_2)
image_1_cv, image_2_cv = convert_to_cv(image_1, image_2)
key_points_1, key_points_2, description_1, description_2 = calculate_features(image_1_cv, image_2_cv)
matches = calculate_matches(description_1, description_2)
#display_matches(image_1_cv, key_points_1, image_2_cv, key_points_2, matches)
list_key_points_1, list_key_points_2 = find_matching_coordinates(key_points_1, key_points_2)
average_feature_distance = calculate_mean_distance(list_key_points_1, list_key_points_2)
speed = calculate_speed_in_kmps(average_feature_distance, 12648, time_difference)
print(speed)