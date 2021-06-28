from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, text
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(Text)
    is_published = Column(Boolean)
    created = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    modified = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
