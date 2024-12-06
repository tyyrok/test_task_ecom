from fastapi import APIRouter

from api.v1.endpoints.form import router as form_router

router = APIRouter(prefix="/v1")

router.include_router(form_router, prefix="", tags=["Form"])
