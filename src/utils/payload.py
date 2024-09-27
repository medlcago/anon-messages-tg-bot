from aiogram.utils import payload


def decode_payload(data: str) -> str | None:
    try:
        result = payload.decode_payload(payload=data)
        return result
    except ValueError:
        return
