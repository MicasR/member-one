from . import models as m
from db.session_handler import session_maker


def create_member_entry(entry_details_dict: dict) -> m.MemberEntry:
    entry = m.MemberEntry(**entry_details_dict)
    with session_maker() as session:
        session.add(entry)
        session.commit()
        session.refresh(entry)
    return entry


def read_member_entry(items_per_page: int, page: int) -> list[m.MemberEntry]:
    with session_maker() as session:
        entries = session.query(m.MemberEntry
        ).order_by(m.MemberEntry.created_at.desc()
        ).slice((page-1) * items_per_page, page * items_per_page
        ).all()
    return entries

