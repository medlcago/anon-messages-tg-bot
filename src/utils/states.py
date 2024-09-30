from aiogram.fsm.state import StatesGroup, State


class Dialog(StatesGroup):
    message = State()
