from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.callback_data import DialogCallback
from utils.states import Dialog

if TYPE_CHECKING:
    from language.translator import LocalizedTranslator

start_dialog_router = Router(name="start_dialog")


@start_dialog_router.callback_query(DialogCallback.filter())
async def start_dialog_callback(callback: CallbackQuery, callback_data: DialogCallback, state: FSMContext, translator: LocalizedTranslator):
    await callback.message.edit_text(
        text=translator.get("start-dialog-message")
    )
    await state.set_state(Dialog.message)
    await state.update_data(telegram_id=callback_data.telegram_id)


@start_dialog_router.message(Dialog.message)
async def start_dialog(message: Message, state: FSMContext, translator: LocalizedTranslator):
    data = await state.get_data()
    telegram_id = data.get("telegram_id")
    try:
        msg = await message.send_copy(
            chat_id=telegram_id
        )

        await msg.reply(
            text=translator.get("new-message"),
        )

        await message.reply(
            text=translator.get("sent-successfully-message"),
        )
    except ValueError:
        await message.reply(
            text=translator.get("unsupported-message")
        )
    finally:
        await state.clear()
