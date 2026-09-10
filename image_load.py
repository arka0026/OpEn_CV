import cv2 
pic=cv2.imread('pikachu.jpg') #laod image
if pic is not None:
    print('image is  loaded')
else:
    print('image loaded')
