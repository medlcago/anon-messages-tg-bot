from abc import abstractmethod, ABC

from pydantic import ConfigDict, BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User


class IUserRepo(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, telegram_id: str, **kwargs) -> User | None:
        raise NotImplementedError


class UserRepo(IUserRepo, BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    session: AsyncSession

    async def create_user(self, user: User) -> User:
        self.session.add(user)
        await self.session.flush([user])
        return user

    async def get_user(self, telegram_id: str, **kwargs) -> User | None:
        stmt = select(User).filter_by(telegram_id=telegram_id, **kwargs)
        user = await self.session.scalar(stmt)
        return user
