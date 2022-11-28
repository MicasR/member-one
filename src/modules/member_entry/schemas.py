from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class MemberEntryStatus(str, Enum):
    registered = "Registered"
    approved = "Approved"
    rejected = "Rejected"


class MemberEntryIn(BaseModel):
    full_name: str
    status: MemberEntryStatus | None = MemberEntryStatus.registered

    class Config:
        orm_mode = True


class MemberEntryOut(MemberEntryIn):
    id: int
    status: MemberEntryStatus
    created_at: datetime
    lst_updated_at: datetime
