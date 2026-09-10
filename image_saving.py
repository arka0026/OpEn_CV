import cv2
pic=cv2.imread("pikachu.jpg")
if pic is not None:
    cv2.imwrite("save_image.jpg",pic) #saveing image
    print('Successful')
else:
    print('not successful')


