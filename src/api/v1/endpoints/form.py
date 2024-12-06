from typing import Union
from fastapi import APIRouter

from services.form import get_form_response
from schemas.form import InputData, FormFoundResponse, FormNotFoundResponse

router = APIRouter()


@router.post(
    "/get_form/", response_model=Union[FormFoundResponse, FormNotFoundResponse]
)
async def get_form(data: InputData) -> dict:
    return await get_form_response(data)
