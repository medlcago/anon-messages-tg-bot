from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram.utils.payload import decode_payload

from core.text import COMMAND_START
from keyboards.inline import main_keyboard

command_start_router = Router(name="start")


@command_start_router.message(CommandStart(deep_link=True))
async def command_start_with_args(message: Message, command: CommandObject):
    payload = decode_payload(command.args)
    await message.answer(f"Your payload: {payload}")


@command_start_router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
        text=COMMAND_START,
        reply_markup=main_keyboard()
    )


@command_start_router.callback_query(F.data == "main_menu")
async def command_start_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=COMMAND_START,
        reply_markup=main_keyboard()
    )
