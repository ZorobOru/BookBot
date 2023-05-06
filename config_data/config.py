from environs import Env
from aiogram import Bot, Dispatcher
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN"),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))))
