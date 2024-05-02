from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import CheckConstraint, ForeignKey, create_engine
import datetime


class Base(DeclarativeBase):
    pass


class Credential(Base):
    __tablename__ = 'credentials'
    email: Mapped[str] = mapped_column(primary_key=True)
    password_hash: Mapped[str]


class Booker(Base):
    __tablename__ = 'bookers'
    __table_args__ = (
        CheckConstraint('role IN ("Venue_Manager","Booker")',
                        name='valid_role'),
    )
    credential: Mapped[str] = mapped_column(
        ForeignKey('credentials.email'))  # ondelelete and onupdate
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
    phone: Mapped[str]
    role: Mapped[str]


class Venue(Base):
    __tablename__ = 'venues'
    name: Mapped[str] = mapped_column(primary_key=True)
    capacity: Mapped[int]
    __table_args__ = (
        CheckConstraint('capacity > 30', name='valid_venue_capacity'),
    )


class Booking(Base):
    __tablename__ = 'bookings'
    __table_args__ = (
        CheckConstraint('status IN ("Available","Occupied")'),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    venue: Mapped[str] = mapped_column(
        ForeignKey('venues.name'))  # ondelete and onupdate
    booked_by: Mapped[int] = mapped_column(
        ForeignKey('bookers.id'))  # ondelete and onupdate
    booked_date: Mapped[datetime.datetime]
    from_: Mapped[datetime.time]
    to_: Mapped[datetime.time]
    reason: Mapped[str]
    released_by: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str]


engine = create_engine('sqlite:///venufinder.db', echo=True)
Base.metadata.create_all(engine)


# print(dir(engine))
# print()
# print()
# print(dir(engine.connect()))
