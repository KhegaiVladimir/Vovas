from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from db.database import Database
from pathlib import Path


load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()
database = Database(Path(__file__).parent / 'db.sqlite')