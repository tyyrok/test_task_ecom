from typing import Dict

from pydantic import RootModel, BaseModel


class InputData(RootModel):
    root: Dict[str, str]


class FormFoundResponse(BaseModel):
    name: str


class FormNotFoundResponse(InputData):
    pass
