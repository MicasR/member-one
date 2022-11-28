from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

Base = declarative_base()


class MemberEntry(Base):
    __tablename__ = "member_entry"

    id = Column("id", Integer, primary_key=True, nullable=False)

    full_name = Column("full_name", String, nullable=False)
    status = Column("status", String, nullable=False)

    created_at = Column("created_at", TIMESTAMP(
        timezone=True), nullable=False, server_default=text('now()'))
    lst_updated_at = Column("lst_updated_at", TIMESTAMP(
        timezone=True), nullable=False, server_default=text('now()'))
