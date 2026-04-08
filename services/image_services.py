import base64
import os

import cv2 as cv
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACE_MODEL_PATH = os.path.join(BASE_DIR, "haarcascade_frontalface_default.xml")
FACE_CASCADE = cv.CascadeClassifier(FACE_MODEL_PATH)



def decode_base64_image(base64_str):
    if "," in base64_str:
        _, encoded = base64_str.split(",", 1)
    else:
        encoded = base64_str  # fallback

    img_bytes = base64.b64decode(encoded)
    np_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv.imdecode(np_arr, cv.IMREAD_COLOR)
    return img

def encode_img_to_base64(img):
    _,buffer = cv.imencode(".jpg",img)
    return base64.b64encode(buffer).decode('utf-8')


def face_detect(image):

    img = decode_base64_image(image)
    if img is None:
        raise ValueError("Invalid image data")

    if FACE_CASCADE.empty():
        raise RuntimeError(f"Haar Cascade not loaded from: {FACE_MODEL_PATH}")


    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    face = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor= 1.1,
        minNeighbors = 5 ,
        minSize = (30,30)
    )

    for(x,y,w,h) in face:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,222,0),2)

    encoded_img = encode_img_to_base64(img)

    return (encoded_img,face)


def resize_img(image):
   
    img = decode_base64_image(image)

    if img is None:
       print(f"image is missing: {image}")
    res = cv.resize(img,None,fx=0.5,fy=0.5,interpolation= cv.INTER_CUBIC)
    
    encoded = encode_img_to_base64(res)

    return encoded


def rotate_img(image):
      
    img = decode_base64_image(image)
    if img is None:
        raise ValueError("Invalid image data")

    rows,cols = img.shape[:2]

    center = (cols //2 ,rows//2)

    M  = cv.getRotationMatrix2D(center,180,1.0)
    dst = cv.warpAffine(img,M,(cols,rows))

    return encode_img_to_base64(dst)


def gray_scale(image):
    ddepth=cv.CV_16S
    kernel_size=3
    window_name = "Laplace"

    img = decode_base64_image(image)
    if img is None:
        print(f"status_code=400, detail=Invalid image data")

    if img is None:
       print(f"image is missing: {image}")

    src = cv.GaussianBlur(img,(3,3),0)

    src_gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

    dst = cv.Laplacian(src_gray,ddepth,ksize=kernel_size)

    abs_dst = cv.convertScaleAbs(dst)
    
    res = encode_img_to_base64(abs_dst)
    return res 


def blur_img(image):
    
    
    
    img = decode_base64_image(image)
    if img is None:
        print(f"status_code=400, detail=Invalid image data")
    
    blur = cv.GaussianBlur(img,(15,15),0)
    
    res = encode_img_to_base64(blur)
    return res


def face_blur(image):
    img = decode_base64_image(image)
    if img is None:
        raise ValueError("Invalid image data")

    if img is None :
        print("image is missing ");


    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    if FACE_CASCADE.empty():
        raise RuntimeError(f"Haar Cascade not loaded from: {FACE_MODEL_PATH}")

    faces = FACE_CASCADE.detectMultiScale(gray,1.1, 5)

    for (x,y,w,h) in faces:

        face_region = img[y:y+h,x:x+w]

        blurred = cv.GaussianBlur(face_region,(99,99),30)

        img[y:y+h,x:x+w] = blurred

    res  = encode_img_to_base64(img)

    return res
     
