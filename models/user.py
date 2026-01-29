from sqlalchemy import create_engine, Column, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .base import Base
import uuid
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)



class Users(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    senha = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    tenant_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tenants.id"),
        nullable=False
    )

    tenant = relationship(
        "Tenant",
        back_populates="users"
    )

