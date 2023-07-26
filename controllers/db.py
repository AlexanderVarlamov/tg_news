from sqlalchemy import create_engine, Integer, Boolean, select, update, DateTime, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session

engine = create_engine("sqlite:///./users.db", echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    dt = mapped_column(DateTime,
                       server_default=func.now(),
                       onupdate=func.now()
                       )

    def __repr__(self):
        return f"User(id={self.id}, user_id={self.user_id}, is_active={self.is_active})"


def add_user(user_id: int):
    with Session(engine) as session:
        new_user = User(user_id=user_id)
        session.add(new_user)
        session.commit()


def get_users():
    with Session(engine) as session:
        users = session.execute(select(User.user_id, User.is_active)).all()
        return users


def set_user_status(user_id: int, status: bool):
    with Session(engine) as session:
        expr = update(User).where(User.user_id == user_id).values(is_active=status).returning(User)
        session.execute(expr)
        session.commit()


def user_is_present(user_id: int):
    with Session(engine) as session:
        expr = select(User).filter_by(user_id=user_id)
        return session.execute(expr).first() is not None


Base.metadata.create_all(engine)

