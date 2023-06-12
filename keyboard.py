"""Keyboard module."""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


Statistic = "Статистика пользователя"
InformationBlock = "Информационный блок"
ShortArticles = "Статьи-пятиминутки"
TrainConstructor = "Конструктор тренировок"
UserLibrary = "Библиотека"

MainMenuMarkup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(Statistic))
    .add(KeyboardButton(InformationBlock))
    .add(KeyboardButton(TrainConstructor))
    .add(KeyboardButton(UserLibrary))
)
