from aiogram.types import CallbackQuery
from aiogram.filters import BaseFilter
import re


class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback_data: CallbackQuery):
        return isinstance(callback_data.data, str) and callback_data.data.isdigit()


class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return re.search(r'.*?\d+del$', callback.data)


class IsSetBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return re.search(r'\d+/\d+', callback.data)