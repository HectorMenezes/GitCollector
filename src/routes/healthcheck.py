from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def healthcheck():
    return {"everything if fine": "right?"}
