from . import schemas as s
from . import datalayer as dl


def create_member_entry(entry_details: s.MemberEntryIn) -> s.MemberEntryOut:
    # validate
    # TODO test this fuction to see what validation are necessary

    # change inputs
    entry_details_dict = entry_details.dict()
    entry_details_dict["status"] = s.MemberEntryStatus.registered

    # add to db
    entry = dl.create_member_entry(entry_details_dict)
    # change outputs
    return s.MemberEntryOut(**entry.__dict__)
