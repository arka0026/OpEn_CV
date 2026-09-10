import cv2
user=input("Enter the image path:-")
pic=cv2.imread(user)
print("What you want?\n" \
"1.Show image\n" \
"2.Save image\n" \
"3.both\n" \
"4.Leave")

while True:
    choose=int(input("Choose one{1,2,3,4}:-"))
    if choose==1:
        if pic is not None:
            cv2.imshow("Here the pic",pic)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("There have some problem")

    elif choose==2:
        if pic is not None:
            cv2.imwrite("Output_image.jpg",pic)
            print("Image saved successfully")
        else:
            print("Image saved not successfully")

    elif choose==3:
        if pic is not None:
            cv2.imshow("Here the pic",pic)
            cv2.imwrite("Output_Image.png",pic)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
        else:
            print("Invalid")

    elif choose==4:
        break

    else:
        print("Enter numbers between (1,2,3,4)" )











