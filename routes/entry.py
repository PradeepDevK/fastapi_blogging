from fastapi import APIRouter

router = APIRouter()

# endpoint
@router.get("/")
def apiRunning():
    response = {
        "status": "OK",
        "message": "API is running."
    }
    return response