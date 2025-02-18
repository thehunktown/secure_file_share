from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.database import Base
import uuid
from sqlalchemy.sql import func

class BaseModel:
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(UUID(as_uuid=True), nullable=False, index=True)  # Multi-tenancy support

    # User-related fields
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    updated_by = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=True)
    deleted_by = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=True)
    
    created_at = Column(DateTime, default=func.now())  # Automatically set the creation time
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Automatically update time on modification
    deleted_at = Column(DateTime, nullable=True)  # Track deletion time
    
    # Relationships to User for created_by, updated_by, deleted_by
    created_user = relationship('User', foreign_keys=[created_by])
    updated_user = relationship('User', foreign_keys=[updated_by])
    deleted_user = relationship('User', foreign_keys=[deleted_by])
