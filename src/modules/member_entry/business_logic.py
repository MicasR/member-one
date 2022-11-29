from . import schemas as s
from . import datalayer as dl

from src import utilis as gu

def create_member_entry(entry_details: s.MemberEntryIn) -> s.MemberEntryOut:
    # validate
    # TODO test this fuction to see what validation are necessary

    # change inputs
    entry_details_dict = entry_details.dict()
    entry_details_dict["status"] = s.MemberEntryStatus.registered

    # interact with db
    entry = dl.create_member_entry(entry_details_dict)

    # change outputs
    result = s.MemberEntryOut(**entry.__dict__)

    return result


def read_member_entries(items_per_page:int , page: int) -> list[s.MemberEntryOut]:
    # validate
    if not gu.paginateable(items_per_page, page): return []

    # change inputs
    if items_per_page > 100: items_per_page = 100

    # interact with db
    entries = dl.read_member_entries(items_per_page, page)

    # change outputs
    result = [s.MemberEntryOut(**entry.__dict__) for entry in entries]
    return result


def read_member_entry(id: int) -> s.MemberEntryOut | None:
    # validate
    if not gu.is_positive_int(id): return None

    # change inputs

    # interact with db
    entry = dl.read_member_entry(id)
    if not entry: return None

    # change outputs
    result = s.MemberEntryOut(**entry.__dict__)

    return result
