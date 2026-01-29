from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()

class EmailCode(Base):
    __tablename__ = "email_codes"

    email = Column(String, primary_key=True)
    code = Column(String)
    expires_at = Column(DateTime)



