'''What objects have an id?
ENTITIES:
    email content
    user
    campaign
'''

'''What are aggregates?
Send email:
    user id
    email content id
    campaign id

Update sent emails
'''

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AbstractEntity(BaseModel):
    id: Optional[int]


class TodoEntry(AbstractEntity):
    summary: str
    detail: Optional[str]



