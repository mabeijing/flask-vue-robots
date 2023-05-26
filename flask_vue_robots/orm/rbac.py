import uuid

from sqlalchemy import BIGINT, INTEGER, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import db, BaseModel


def generate_uuid() -> int:
    return uuid.uuid1().int


class TBRoles(BaseModel):
    __tablename__ = 'tb_roles'
    id: Mapped[int] = mapped_column(BIGINT, name='ID', primary_key=True, autoincrement=True, comment="主键")
    role_id = db.Column(db.BIGINT, name="ROLE_ID", unique=True, nullable=False, comment="角色ID")
    role_name: Mapped[str] = mapped_column(String(32), nullable=False, comment="角色名字")
    father_id: Mapped[int] = mapped_column(INTEGER, default=0, comment="父ID")
    users: Mapped[list["TBUsers"]] = relationship(back_populates="role")

    def to_dict(self):
        return {
            "id": self.id,
            "role_id": self.role_id,
            "role_name": self.role_name,
            "father_id": self.father_id
        }


class TBUsers(BaseModel):
    __tablename__ = 'tb_users'
    id: Mapped[int] = mapped_column(BIGINT, name='ID', primary_key=True, autoincrement=True, comment="主键")
    user_id: Mapped[int] = mapped_column(String(128), name="USER_ID", unique=True, index=True, default=generate_uuid,
                                         comment="用户ID")
    username: Mapped[str] = mapped_column(String(32), name="USER_NAME", nullable=False, comment="用户名")
    password: Mapped[str] = mapped_column(String(256), name="PASSWORD", comment="密码")
    nick_name: Mapped[str] = mapped_column(String(128), name="NICK_NAME", comment="昵称")
    email: Mapped[str] = mapped_column(String(64), name="EMAIL", comment="邮箱")
    avatar: Mapped[str] = mapped_column(String(128), name="AVATAR", comment="头像")
    role_id: Mapped[int] = mapped_column(ForeignKey(f"{TBRoles.__tablename__}.ROLE_ID"))
    role: Mapped["TBRoles"] = relationship(TBRoles, back_populates="users")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "nick_name": self.nick_name,
            "email": self.email,
            "avatar": self.avatar,
            "role": self.role.to_dict()
        }
