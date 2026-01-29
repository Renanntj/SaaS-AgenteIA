from sqlalchemy import Column, String, Integer, DateTime
from .base import Base
from sqlalchemy import Column, String, DateTime



class EmailCode(Base):
    __tablename__ = "email_codes"

    email = Column(String, primary_key=True)
    code = Column(String)
    expires_at = Column(DateTime)



