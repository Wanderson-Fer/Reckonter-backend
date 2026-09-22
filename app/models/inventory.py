import datetime as dt
from sqlalchemy import ForeignKey, DateTime, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.models import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_product: Mapped[int] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[float]
    last_update: Mapped[DateTime] = mapped_column(DateTime, default=dt.datetime.now())
    location: Mapped[str] = mapped_column(String(30), nullable=True)
