from datetime import date, datetime

from sqlalchemy import String, ForeignKey, Date, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Destination(Base):
    __tablename__ = "destinations"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(50))
    climate: Mapped[str] = mapped_column(String(30))
    budget_level: Mapped[str] = mapped_column(String(10))

    # many-to-many relationship
    interests: Mapped[list["Interest"]] = relationship(
        secondary="destination_interests",
        back_populates="destinations"
    )


class Interest(Base):
    __tablename__ = "interests"

    id: Mapped[int] = mapped_column(primary_key=True)
    interest: Mapped[str] = mapped_column(String(50), unique=True)

    # many-to-many relationship
    destinations: Mapped[list["Destination"]] = relationship(
        secondary="destination_interests",
        back_populates="interests"
    )

class DestinationInterest(Base):
    __tablename__ = "destination_interests"

    destination_id: Mapped[int] = mapped_column(
        ForeignKey("destinations.id"),
        primary_key=True
    )
    interest_id: Mapped[int] = mapped_column(
        ForeignKey("interests.id"),
        primary_key=True
    )


class CachedSearch(Base):
    __tablename__ = "cached_searches"

    query_hash: Mapped[str] = mapped_column(
        String(64),
        primary_key=True
    )
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    budget_level: Mapped[str] = mapped_column(String(10))
    climate: Mapped[str] = mapped_column(String(30))
    raw_user_input: Mapped[str] = mapped_column(Text)
    normalized_interests: Mapped[str] = mapped_column(Text)
    gemini_output: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
