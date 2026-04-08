# This file is just for Testing perpouse   Api services are in image_services.py file

import os

import cv2 as cv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "arrow.jpg")




def resize_img(image_path):
    img = cv.imread(image_path)
    if img is None:
       print(f"image is missing: {image_path}")
    res = cv.resize(img,None,fx=0.5,fy=0.5,interpolation= cv.INTER_CUBIC)
    cv.imshow("Original" , img)
    cv.imshow("Resized",res)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rotate_img(imgage_path):
      img = cv.imread(imgage_path)
      rows,cols = img.shape[:2]
    #   print(f"rows : {rows}  cols : {cols} ")

      center = (cols //2 ,rows//2)

    #   print(f"rows //2 : {rows//2}  cols//2 : {cols//2}   center = {center}")

      M  = cv.getRotationMatrix2D(center,180,1.0)
      dst = cv.warpAffine(img,M,(cols,rows))

      cv.imshow("Original" , img)
      cv.imshow("Resized",dst)
      cv.waitKey(0)
      cv.destroyAllWindows()

# rotate_img(IMAGE_PATH)
def gray_scale(image_path):
    ddepth=cv.CV_16S
    kernel_size=3
    window_name = "Laplace"

    img = cv.imread(image_path)
    if img is None:
       print(f"image is missing: {image_path}")

    src = cv.GaussianBlur(img,(3,3),0)

    src_gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

    dst = cv.Laplacian(src_gray,ddepth,ksize=kernel_size)

    abs_dst = cv.convertScaleAbs(dst)

    cv.imshow(window_name,abs_dst)
    cv.imshow("src",src)
    # cv.imshow("src-gray",src_gray)
    cv.waitKey(0)


def blur_img(image_path):

    img = cv.imread(image_path)
    if img is None:
        print('Image path is wronge or mising')
    
    blur = cv.GaussianBlur(img,(15,15),0)

    cv.imread("Original", img)
    cv.imshow("Blurred", blur)

    cv.waitKey(0)
    cv.destroyAllWindows()


def face_blur(image_path,):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    faceModel = os.path.join(BASE_DIR, "haarcascade_frontalface_default.xml")


    img = cv.imread(image_path)

    face_cascade = cv.CascadeClassifier(faceModel)

    if img is None :
        print("image is missing ");


    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1, 5)

    for (x,y,w,h) in faces:

        face_region = img[y:y+h,x:x+w]

        blurred = cv.GaussianBlur(face_region,(99,99),30)

        img[y:y+h,x:x+w] = blurred

    
    cv.imshow("Blurred Face", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


face_blur(IMAGE_PATH)