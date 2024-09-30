from __future__ import annotations

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.callback_data import DialogCallback
from utils.states import Dialog

start_dialog_router = Router(name="start_dialog")


@start_dialog_router.callback_query(DialogCallback.filter())
async def start_dialog_callback(callback: CallbackQuery, callback_data: DialogCallback, state: FSMContext):
    await callback.message.edit_text(
        text="Напишите сообщение, которое вы хотите отправить анонимно\n\nЕсли вы передумали, используйте /cancel, чтобы отменить текущее состояние"
    )
    await state.set_state(Dialog.message)
    await state.update_data(telegram_id=callback_data.telegram_id)


@start_dialog_router.message(Dialog.message)
async def start_dialog(message: Message, state: FSMContext):
    data = await state.get_data()
    telegram_id = data.get("telegram_id")
    try:
        msg = await message.send_copy(
            chat_id=telegram_id
        )

        await msg.reply(
            text="🔔 Вам пришло новое сообщение",
        )

        await message.reply(
            text="Сообщение успешно отправлено ✅",
        )
    except ValueError:
        await message.reply(
            text="К сожалению, данный тип сообщений не поддерживается 😔"
        )
    finally:
        await state.clear()
