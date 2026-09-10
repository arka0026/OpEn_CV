import cv2
path=input("enter the image path:-")
pic=cv2.imread(path)
if pic is not None:
    print("image is loaded")

    cv2.imshow('here the image',pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('image not loaded')