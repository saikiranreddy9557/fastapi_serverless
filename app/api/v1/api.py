from fastapi import APIRouter
from .endpoint import services

router = APIRouter()

router.include_router(router=services.router,prefix="/test",tags=["endpoint test"])