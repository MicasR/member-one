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


@router.get("/", response_model=list[s.MemberEntryOut])
async def read_posts(items_per_page: int = 15, page: int = 1):
    entries = bl.read_member_entries(items_per_page, page)
    return entries
