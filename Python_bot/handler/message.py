import requests
from aiogram.types import Message
from aiogram import Router
from config import kurslar
from aiogram.filters import  Command



msg_router = Router()

@msg_router.message()
async def convert_money(message: Message):
    try:
        x = int(message.text)
        s = f"{x} so'm: \n"
        s += f"\t-{x / kurslar ['USD']: .2f} dollar\n" 
        s += f"\t-{x / kurslar ['EUR']: .2f} yevro\n"
        s += f"\t-{x / kurslar ['RUB']: .2f} rubl ga teng bo'ladi."
        await message.reply(text=s)
    except:
        await message.reply("Iltimos faqat son kiriting yoki /help tugmasidan foydalaning.")