from __future__ import print_function
import argparse as ap
import cv2
import imutils 
import numpy as np
import os
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from scipy.cluster.vq import *
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import itertools
from sklearn.model_selection import learning_curve
from collections import Counter
import serial
from time import sleep
import sys
from skimage.feature import peak_local_max
from scipy import ndimage

# Load the classifier, class names, scaler, number of clusters and vocabulary 
clf, classes_names, stdSlr, k, voc = joblib.load("svc.pkl")

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# Get the path of the testing set
parser = ap.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--testingSet", help="Path to testing Set")
group.add_argument("-i", "--image", help="Path to image")
parser.add_argument('-v',"--visualize", action='store_true')
args = vars(parser.parse_args())

# Get the path of the testing image(s) and store them in a list
image_paths = []
test_arr = []
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
if args["testingSet"]:
    test_path = args["testingSet"]
    try:
        testing_names = os.listdir(test_path)
    except OSError:
        print ('No such directory {}\nCheck if the file exists')
        exit()
    for testing_name in testing_names:
        dir = os.path.join(test_path, testing_name)
        class_path = imutils.imlist(dir)
        image_paths+=class_path
        #print testing_name
	list = os.listdir(dir) # dir is your directory path
	def last_4chars(x):
            return(x[-4:])
        a = sorted(list, key = last_4chars)
	number_files = len(a)
	#print number_files
	for iter in range(0 , number_files):
		test_arr.append(testing_name)

else:
	image_paths = [args["image"]]
    
# Create feature extraction and keypoint detector objects
fea_det = cv2.FeatureDetector_create("SIFT")
des_ext = cv2.DescriptorExtractor_create("SIFT")

# List where all the descriptors are stored
des_list = []

for image_path in image_paths:
    im = cv2.imread(image_path)
    im = cv2.cvtColor( im, cv2.COLOR_RGB2GRAY )
    im = clahe.apply(im)

    kpts = fea_det.detect(im)
    kpts, des = des_ext.compute(im, kpts)
    des_list.append((image_path, des))  
    
# Stack all the descriptors vertically in a numpy array
descriptors = des_list[0][1]
for image_path, descriptor in des_list[0:]:
    descriptors = np.vstack((descriptors, descriptor)) 

# k-means clustering
test_features = np.zeros((len(image_paths), k), "float32")
for i in xrange(len(image_paths)):
    words, distance = vq(des_list[i][1],voc)
    for w in words:
        test_features[i][w] += 1

# Perform Tf-Idf vectorization
nbr_occurences = np.sum( (test_features > 0) * 1, axis = 0)
idf = np.array(np.log((1.0*len(image_paths)+1) / (1.0*nbr_occurences + 1)), 'float32')

# Scale the features
test_features = stdSlr.transform(test_features)

# Perform the predictions
predictions =  [classes_names[i] for i in clf.predict(test_features)]


# Visualize the coordinates of the results, if "visualize" flag set to true by the user
if args["visualize"]:
    for image_path, prediction in zip(image_paths, predictions):
        image = cv2.imread(image_path)
        filename = os.path.basename(image_path)
        index_of_dot = filename.index('.')
        filename2 = filename[:index_of_dot]
        print (prediction.ljust(13) + "-- " +  filename2)
        
        #cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        #pt = (0, 3 * image.shape[0] // 4)
        #cv2.putText(image, prediction, pt ,cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, [0, 255, 0], 2)
        #cv2.imshow("Image", image)
        #cv2.waitKey(2000)

#Counter        
count = Counter(predictions)
print (count)        

#Weight
COM = 'COM5'# /dev/ttyACM0 (Linux)
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

#check args
if("-t" in sys.argv or "--testingSet" in sys.argv):
	testingSet = True
else:
	testingSet= False

while True:
	val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
	valA = val.split("/")
	#print()
	if(testingSet == True):
		print(val, end="\r")
		sys.stdout.flush()
	
