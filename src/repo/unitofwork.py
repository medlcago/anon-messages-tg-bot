from typing import Self, Any

from pydantic import Field, BaseModel, ConfigDict
from sqlalchemy.ext.asyncio import AsyncSession

from repo.user_repo import IUserRepo, UserRepo


class UnitOfWork(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    session: AsyncSession
    user_repo: IUserRepo = Field(default=None, init=False)

    def model_post_init(self, __context: Any) -> None:
        self.user_repo = UserRepo(session=self.session)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            await self.commit()
        else:
            await self.rollback()
        await self.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    async def close(self):
        await self.session.close()
