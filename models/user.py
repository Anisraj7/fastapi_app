from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.database import Base


class User(Base):
    __tablename__ = "users"
