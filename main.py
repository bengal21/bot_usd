from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.dispatcher import filters
from tok import token_telegram
from api_exchenge import get_rate_usd

bot = Bot(token=token_telegram)
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup()
keyboard.add("Обновить курс доллара")


@dp.message_handler(commands="start")
async def start(message):
    await message.answer("Добрый день. Как вас зовут?")


@dp.message_handler(filters.Text(equals=["Обновить курс доллара"]))
async def on_gaz(message):
    if type(get_rate_usd()) == float:
        await message.answer(f'Курс доллара на сейчас {get_rate_usd()} руб.')
    else:
        await message.answer(get_rate_usd())


@dp.message_handler()
async def on_volume(message):
    if type(get_rate_usd()) == float:
        await message.answer(f'Рад знакомству, {message.text}! Курс доллара на сегодня {get_rate_usd()} руб.',
                             reply_markup=keyboard)
    else:
        await message.answer(get_rate_usd())


executor.start_polling(dp, skip_updates=True)
