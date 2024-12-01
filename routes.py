from fastapi import APIRouter, File, UploadFile, HTTPException
from sinusitis_detection_and_severity_classification import process_uploaded_file
import logging

router = APIRouter()

# Test route to check server status
@router.get("/test")
async def testAPI():
    """
    Test route to check if the API server is running.
    """
    return {"message": "Server is running and working fine!"}

# Define the API endpoint for predictions
@router.post("/predict")
async def predictAPI(file: UploadFile = File(...)):
    """
    Endpoint to upload a file for sinusitis detection and severity classification.

    - **file**: The image file for sinusitis detection.
    """
    try:
        # Process the uploaded file and return prediction results
        result = await process_uploaded_file(file)
        return {"prediction": result}
    except Exception as e:
        # Return error details in case of failure
        logging.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

