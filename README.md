# OpenCV FastAPI Backend

This repository contains a FastAPI backend for basic image processing with OpenCV. It accepts base64-encoded images, applies an operation, and returns the processed image as a base64 data URL.

## Features

- Face detection with bounding boxes
- Full-image Gaussian blur
- Image resize
- 180 degree image rotation
- Grayscale Laplacian-style effect
- CORS enabled for local frontend development

## Tech Stack

- Python 3.14+
- FastAPI
- Uvicorn
- OpenCV
- NumPy
- uv

## Project Structure

```text
.
|-- main.py
|-- pyproject.toml
|-- uv.lock
|-- haarcascade_frontalface_default.xml
|-- services/
|   |-- image_services.py
|   |-- image_services_testesting.py
|   `-- arrow.jpg
`-- README.md
```

## Requirements

- Python 3.14 or newer
- `uv` installed

Install `uv` if needed:

```powershell
pip install uv
```

## Installation

```powershell
uv sync
```

## Run The Server

```powershell
uv run uvicorn main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

Interactive docs are available at:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### `POST /`

Health check endpoint.

Response:

```json
{
  "message": "OpenCV backend is running"
}
```

### `POST /detect`

Detects faces and draws green rectangles around them.

Request body:

```json
{
  "image": "data:image/jpeg;base64,..."
}
```

Response:

```json
{
  "image": "data:image/jpeg;base64,...",
  "faces": 1
}
```

### `POST /blur`

Applies Gaussian blur to the whole image.

### `POST /resize`

Resizes the image to 50 percent of its original width and height.

### `POST /rotate`

Rotates the image by 180 degrees.

### `POST /gray`

Applies a grayscale Laplacian-style effect.

## Example Request

```javascript
const response = await fetch("http://localhost:8000/detect", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    image: "data:image/jpeg;base64,..."
  })
});

const data = await response.json();
console.log(data);
```

## Notes

- Face detection uses `haarcascade_frontalface_default.xml`.
- The frontend should send images as base64 data URLs.
- If the cascade file is missing or invalid, face detection will fail during request processing.

## Development Notes

- `services/image_services.py` contains the API-facing image processing functions.
- `services/image_services_testesting.py` is a local OpenCV experimentation script and is not used by the API server.

## Common Issues

### `AttributeError: 'str' object has no attribute 'empty'`

This happens if the Haar cascade XML path is treated like a loaded OpenCV classifier. The backend should load the cascade with `cv.CascadeClassifier(...)` before calling `.empty()` or `.detectMultiScale(...)`.

### Frontend cannot connect to backend

- Make sure the backend is running on port `8000`.
- Make sure the frontend is calling `http://localhost:8000`.
- Check the browser console and FastAPI terminal logs for request errors.

## License

Add your preferred license before publishing publicly if you want to define how others may use the code.
