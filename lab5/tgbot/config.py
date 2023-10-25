from dataclasses import dataclass

from environs import Env


@dataclass
class Telegram:
    token: str


@dataclass
class Config:
    telegram: Telegram


def load_config():
    env = Env()

    return Config(
        telegram=Telegram(
            token=env.str("BOT_TOKEN"),
        ),
    )
