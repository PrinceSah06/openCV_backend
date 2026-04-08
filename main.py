from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from services.image_services import blur_img, face_detect, gray_scale, resize_img, rotate_img





app = FastAPI(
    title="OpenCV FastAPI Backend",
    description="Simple image-processing API for face detection and image effects.",
    version="0.1.0",
)

 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers = ["*"]
)








class ImageData(BaseModel):
    image: str



    
@app.post("/")
def home():
    return {"message": "OpenCV backend is running"}

@app.post("/detect")
def face_detection(data: ImageData):
    try:
        encoded_img, face = face_detect(data.image)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return {
        "image": f"data:image/jpeg;base64,{encoded_img}",
        "faces": len(face),
    }


@app.post("/blur")
def blur(data: ImageData):
    encoded_img = blur_img(data.image)
    return {
            "image": f"data:image/jpeg;base64,{encoded_img}"
    }

@app.post("/resize")
def resize(data: ImageData):
    encoded_img = resize_img(data.image)
    return {
            "image": f"data:image/jpeg;base64,{encoded_img}"
    }

@app.post("/rotate")
def rotate(data: ImageData):
    encoded_img = rotate_img(data.image)
    return {
            "image": f"data:image/jpeg;base64,{encoded_img}"
    }

@app.post("/gray")
def gray(data: ImageData):
    encoded_img = gray_scale(data.image)
    return {
            "image": f"data:image/jpeg;base64,{encoded_img}"
    }
