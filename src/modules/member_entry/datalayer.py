from . import models as m
from db.session_handler import session_maker


def create_member_entry(entry_details_dict: dict)-> m.MemberEntry:
    entry = m.MemberEntry(**entry_details_dict)
    with session_maker() as session:
        session.add(entry)
        session.commit()
        session.refresh(entry)
    return entry
