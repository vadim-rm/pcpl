from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dice_button_text = "Бросить кубик"
bowl_button_text = "Сыграть в боулинг"
dart_button_text = "Сыграть в дартс"


def menu_keyboard() -> ReplyKeyboardMarkup:
    return (
        ReplyKeyboardMarkup(resize_keyboard=True)
        .row(
            KeyboardButton(text=dice_button_text),
        )
        .row(
            KeyboardButton(text=dart_button_text),
        )
        .row(
            KeyboardButton(text=bowl_button_text),
        )
    )
