from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session, Session


# 测试提交网速
class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]] = mapped_column(String(30))
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


if __name__ == '__main__':
    from sqlalchemy.engine import create_engine
    from sqlalchemy import URL

    url_object = URL.create(
        "mysql+pymysql",
        username="root",
        password="root@123",
        host="localhost",
        port=3306,
        database="flask-vue-robots",
    )

    engine = create_engine(url_object, pool_recycle=3600, echo=True)
    # 调用create_all来创建表结构，已经存在的表将被忽略
    Base.metadata.create_all(engine)
