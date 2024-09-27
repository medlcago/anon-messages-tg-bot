from __future__ import annotations

from typing import TYPE_CHECKING

from services.user_service import UserService

if TYPE_CHECKING:
    from repo.unitofwork import UnitOfWork


class Service:
    def __init__(self, uow: UnitOfWork):
        self.user_service = UserService(uow=uow)
