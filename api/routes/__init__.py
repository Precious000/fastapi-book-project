from fastapi import APIRouter
from .books import router as books_router
from .stage2 import router as stage2_router  # Import the new router

router = APIRouter()
router.include_router(books_router)
router.include_router(stage2_router)  # Register the new route

