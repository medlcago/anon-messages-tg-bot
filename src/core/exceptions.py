from core.text import INVALID_LINK, SELF_MESSAGE_ATTEMPT


class BotException(Exception):
    message = "❗️Что-то пошло не так. Пожалуйста, повторите попытку позже❗️"

    def __str__(self):
        return self.message


class InvalidPayloadException(BotException):
    message = INVALID_LINK


class SelfMessageAttemptException(BotException):
    message = SELF_MESSAGE_ATTEMPT
