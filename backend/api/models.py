
from typing import Optional, List
from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime


class Blog(BaseModel):
    uid: str = Field(default_factory=uuid4)
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.now)
