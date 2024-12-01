# Medical Image Analysis API

This repository contains an API built using **FastAPI** for medical image analysis. It includes deep learning models.

The application is designed for easy deployment and can be accessed externally using **Ngrok** for testing from mobile or other devices.

---

## Features



---

## Requirements

- **Python 3.7+**
- **Required Libraries**:
  - `FastAPI`
  - `Uvicorn`
  - `TensorFlow`
  - `python-multipart` (for handling file uploads)
  - `Pillow` (for image processing)
  - `numpy` (for numerical operations)
  - `opencv-python` (for image preprocessing)

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

```bash
uvicorn server:app --reload --port 4000
```