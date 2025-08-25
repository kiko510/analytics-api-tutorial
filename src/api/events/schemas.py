from typing import List, Optional
from pydantic import BaseModel, Field


class EventSchema(BaseModel):
    id: int
    page: str | None = ""
    description: str | None = ""
    
class EventCreateSchema(BaseModel):
    page: str
    description: str | None = Field(default="default description")
    
class EventUpdateSchema(BaseModel):
    description: str
    
    
class EventListSchema(BaseModel):
    results: list[EventSchema]
    count: int