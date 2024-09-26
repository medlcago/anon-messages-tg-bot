from aiogram import Router
from aiogram.types import Message, ReactionTypeEmoji

any_message_router = Router(name="any_message")

"""
{
    '🔥': "5104841245755180586",
    '👍': "5107584321108051014",
    '👎': "5104858069142078462",
    '❤️': "5044134455711629726",
    '🎉': "5046509860389126442",
    '💩': "5046589136895476101"
}
"""


@any_message_router.message()
async def any_message(message: Message):
    msg = await message.send_copy(
        chat_id=message.chat.id,
        message_effect_id="5104841245755180586",
    )
    await msg.react(reaction=[ReactionTypeEmoji(emoji="🥰")])
