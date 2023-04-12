from dataclasses import dataclass
from environs import Env


@dataclass
class Hash:
    hash_list = []


@dataclass
class LoadConf:
    url: str
    count_iter: int
    temp_folder: str


@dataclass
class Config:
    load_conf: LoadConf


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        load_conf=LoadConf(
            url=env.str("URL"),
            count_iter=env.int("COUNT_ITER"),
            temp_folder=env.str("TEMP_FOLDER")
        )
    )
