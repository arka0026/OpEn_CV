import cv2 
pic=cv2.imread('pikachu.jpg') #laod image
if pic is not None:

    print('image is loaded')


    cv2.imshow('That is ur image',pic) #opening image
    cv2.waitKey(0) #the image remains open until press any key
    cv2.destroyAllWindows() #closing the image
else:
    print('image not loaded')

