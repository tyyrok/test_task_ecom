from typing import Optional

from fastapi.concurrency import run_in_threadpool
from tinydb import TinyDB

from constants.form import FieldType
from schemas.form import InputData, FormFoundResponse, FormNotFoundResponse
from utilities.validators import (
    validate_date,
    validate_email,
    validate_phone_number,
)

db = TinyDB("src/db.json")


async def get_form_response(schema: InputData) -> None:
    fields = schema.model_dump()
    fields = await get_value_types(fields)
    if found_name := await get_record(fields):
        return FormFoundResponse(name=found_name)
    return FormNotFoundResponse(fields)


async def get_value_types(schema: dict) -> dict:
    for key, value in schema.items():
        if await validate_date(value):
            schema[key] = FieldType.date
        elif await validate_phone_number(value):
            schema[key] = FieldType.phone
        elif await validate_email(value):
            schema[key] = FieldType.email
        else:
            schema[key] = FieldType.text
    return schema


async def get_record(fields: dict) -> Optional[str]:
    all_records = await run_in_threadpool(db.all)
    return await filter_records(all_records, fields)


async def filter_records(
    all_records: list[dict], condition: dict
) -> Optional[str]:
    best_form = None
    for record in all_records:
        name = record.pop("name")
        if record.items() <= condition.items():
            form_len = len(record.keys())
            if not best_form or best_form[0] < form_len:
                best_form = (form_len, name)
    return best_form[1] if best_form else None
