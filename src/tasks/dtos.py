from pydantic import BaseModel


class taskshchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False