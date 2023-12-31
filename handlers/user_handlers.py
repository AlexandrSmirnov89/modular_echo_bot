from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

router = Router()


@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command('help'))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
