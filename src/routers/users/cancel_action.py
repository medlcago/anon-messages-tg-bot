from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from core.logger import logger
from keyboards.inline import action_close_keyboard

cancel_action_router = Router(name="cancel_action")


@cancel_action_router.message(Command("cancel"), any_state)
@cancel_action_router.callback_query(F.data == "cancel", any_state)
async def cancel(event: Message | CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logger.info("Cancelling state %r", current_state)
    await state.clear()
    if isinstance(event, Message):
        await event.answer(
            text="Cancelled.",
            reply_markup=ReplyKeyboardRemove(),
        )
    else:
        await event.message.edit_text(
            text="Cancelled.",
            reply_markup=action_close_keyboard()
        )


@cancel_action_router.callback_query(F.data == "close")
async def close(callback: CallbackQuery):
    await callback.message.delete()
