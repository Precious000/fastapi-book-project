from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def welcome():
    return JSONResponse(content={"message": "Hello, World!"}, status_code=status.HTTP_200_OK)