#imports 

import cv2
import uuid
import os
import time


#defining labels

labels = ['up','down','peace','yo'] #multiclass classification
labels = ['peace']
num_imgs = 5 #number of images of each class


imgs_path = os.path.join('training_images')

if not os.path.exists(imgs_path):
	if os.name == 'nt': #name of windows os is nt....try print(os.name)
		os.mkdir(imgs_path)
	#if os.name == 'posix': #name of linux os is posix....try print(os.name)
		#!mkdir -p {imgs_path}
for label in labels: #labels is our list of custom classes
	label_path = os.path.join(imgs_path, label)
	if not os.path.exists(label_path):
		os.mkdir(label_path)

for label in labels:
	cap = cv2.VideoCapture(0) #capture images from webcam using opencv
	print(f"Collecting images for {label}")
	time.sleep(5)
	for img_num in range(num_imgs):
		print(f"Collecting image number {img_num +1}")
		ret,frame=cap.read()
		
		img_name = os.path.join(imgs_path,label, label + '.' + f'{str(uuid.uuid1())}.jpg') #unique identifier for name of each image
		
		cv2.imwrite(img_name, frame)
		cv2.imshow('frame', frame)
		time.sleep(2)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
cap.release()
cv2.destroyAllWindows()

