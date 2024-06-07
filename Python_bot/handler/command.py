import requests
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from config import kurslar

cmd_router = Router()

@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    a = "Assalomu alekum valyuta botimizga xush kelibsiz!\nYordam uchun /help tugmasini bosing."
    
    await message.answer(a)

@cmd_router.message(Command('help'))
async def cmd_help(message: Message):
    a = "Quyidagi komandalar orqali botdan samarali foydalanishingiz mumkin.\n\n"
    a+= "\t/kurslar - valyuta kurslarini bilish\n "
    a+= "\t/dollar - dollar kursini bilish\n"
    a+= "\t/yevro - yevro kursini bilish\n "
    a+= "\t/rubl - rubl kursini bilish\n\n"
    a+= "Agar biror summani yuborsangiz, bot uni turli valyutalarda sizga hisoblab berishi mumkin.(Masalan: 100000)"

    await message.answer(a)

@cmd_router.message(Command('kurslar'))
async def cmd_kurslar(message: Message):
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')   
    a = "Bugungi valyuta kurslari.\n"
    for kurs in response.json():
        if kurs['Ccy'] in ['USD', 'EUR', 'RUB']:
            kurslar[kurs['Ccy']] = float(kurs['Rate'])
            a += f" 1 {kurs['CcyNm_UZ']} - {kurs['Rate']} so'm \n"

    await message.answer(a)

@cmd_router.message(Command('dollar'))
async def cmd_dollar(message: Message):
    a = f" 1 Aqsh dollari = {kurslar['USD']} so'm "
    await message.reply(a)


@cmd_router.message(Command('yevro'))
async def cmd_yevro(message: Message):
    a = f" 1 Yevro = {kurslar['EUR']} so'm "
    await message.reply(a)


@cmd_router.message(Command('rubl'))
async def cmd_rubl(message: Message):
    a = f" 1 Rossiya rubli = {kurslar['RUB']} so'm "
    await message.reply(a)


async def send_default_message(message: Message):
    await message.reply("Uzr, bu xabar noto'g'ri yoki tushunarsiz. Iltimos, amal qiladigan buyrug'ni kiriting.")