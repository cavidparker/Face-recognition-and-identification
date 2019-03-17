import os #it's a python library to import all the images that are saved in the folder named as dataSet
import cv2 # library
import numpy as np 
from PIL import Image #to capture images
recognizer = cv2.face.LBPHFaceRecognizer_create(); #create a recognizer, LBPH is a face recognition algorithm.Local Binary Patterns Histograms 
path='dataSet'  #path of the image sample where the images are saved
def getImagesWithID(path): # a method to get all the corresponding images with id which means the saved images name
 	imagePaths=[os.path.join(path,f) for f in os.listdir(path)] #create a list for the path for all the images that are available in the folder
 	print (imagePaths) # this is for running this file to check if tha path of the images has created or not

getImagesWithID(path)