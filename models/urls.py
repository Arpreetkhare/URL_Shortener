from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey,Float, Enum,DateTime
from database import DBBase

   

class Urls(DBBase):
    __tablename__ = 'urls'
    short_code: Mapped[str] = mapped_column(String(6), primary_key=True)
    long_url:Mapped[str] = mapped_column(String,nullable=False)

   