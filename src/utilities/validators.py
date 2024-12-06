import re

from pydantic import ValidationError

from schemas.field import date_adapter, email_adapter


async def validate_date(value: str) -> bool:
    try:
        date_adapter.validate_python(value)
    except ValidationError:
        return False
    return True


async def validate_phone_number(value: str) -> bool:
    value = value.replace(" ", "")
    return re.match(r"^\+\d{11}$", value)


async def validate_email(value: str) -> bool:
    try:
        email_adapter.validate_python(value)
    except ValidationError:
        return False
    return True
