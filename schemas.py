from pydantic import BaseModel, Field
from datetime import datetime


''' Model Schema Using Pydantic '''


class Post(BaseModel):
    id: int = Field(default=None)
    title: str = Field()
    body: str = Field()
    is_published: bool = Field(default=False)
    created: datetime = Field(default=None)
    modified: datetime = Field(default=None)

    class Config:
        orm_mode = True
