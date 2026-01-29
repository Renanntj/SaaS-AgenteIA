from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Date, Text
from .base import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import os
import uuid

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    users = relationship(
        "Users",
        back_populates="tenant",
        cascade="all, delete-orphan"
    )
    name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    
    plan_name = Column(String(50), default="free", nullable=False)
    daily_token_limit = Column(Integer, default=5_000, nullable=False)
    monthly_token_limit = Column(Integer, default=100_000, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())



class Usage(Base):
    __tablename__ = "usage"

    from sqlalchemy import UniqueConstraint

    __table_args__ = (
        UniqueConstraint("tenant_id", "date", name="uq_usage_tenant_date"),
    )

    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)

    tokens_used = Column(Integer, default=0, nullable=False)
    messages_count = Column(Integer, default=0, nullable=False)

    date = Column(Date, nullable=False)
    
class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID, ForeignKey("tenants.id"))
    phone_number = Column(String(20))
    role = Column(String(10))  # user | bot
    content = Column(Text)
    created_at = Column(DateTime, server_default=func.now())


