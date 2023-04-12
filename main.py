import asyncio

from src.config import load_config
from src.config import Hash
from src.loader import download_repository
from src.hash_utils import hash_calculator


async def main():
    config = load_config(".env")
    hash_list = Hash.hash_list
    tasks = [download_repository(config.load_conf.url, config.load_conf.temp_folder, hash_list) for _ in
             range(config.load_conf.count_iter)]
    await asyncio.gather(*tasks)
    hash_calculator(config.load_conf.temp_folder, hash_list)


if __name__ == '__main__':
    asyncio.run(main())
