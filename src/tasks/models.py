from sqlalchemy import Column, Integer, String, Boolean
from src.utils.db import base

class taskmodel(base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    is_completed = Column(Boolean, default=False)
    