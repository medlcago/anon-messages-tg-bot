from typing import Any

from pydantic import Field, ConfigDict, BaseModel

from repo.unitofwork import UnitOfWork
from services.user_service import UserService, IUserService


class ServiceContainer(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    uow: UnitOfWork
    user_service: IUserService = Field(default=None, init=False)

    def model_post_init(self, __context: Any) -> None:
        self.user_service = UserService(uow=self.uow)
