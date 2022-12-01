from fastapi import APIRouter, status, HTTPException
from . import schemas as s
from . import business_logic as bl
from src.http_status import responses as cres


router = APIRouter(
    prefix="/member-entry",
    tags=["member-entry"],
    responses= cres  # type: ignore
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=s.MemberEntryOut)
async def create_member_entry(member_entry_schema: s.MemberEntryIn):
    new_entry = bl.create_member_entry(member_entry_schema)
    return new_entry


@router.get("/", response_model=list[s.MemberEntryOut])
async def read_member_entries(items_per_page: int = 15, page: int = 1):
    entries = bl.read_member_entries(items_per_page, page)
    return entries


@router.get("/{id}", response_model=s.MemberEntryOut)
async def read_member_entry(id: int):
    entry = bl.read_member_entry(id)
    if not entry: 
        raise HTTPException(status_code=404, detail=cres[404]["description"])
    return entry


@router.put("/{id}", response_model=s.MemberEntryOut)
async def update_member_entry(id: int, member_entry_schema: s.MemberEntryIn):
    pass
