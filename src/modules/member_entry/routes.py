from fastapi import APIRouter, status
from . import schemas as s
from . import business_logic as bl

router = APIRouter(
    prefix="/member-entry",
    tags=["member-entry"],
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=s.MemberEntryOut)
async def create_member_entry(member_entry_schema: s.MemberEntryIn):
    new_entry = bl.create_member_entry(member_entry_schema)
    return new_entry
