import aiohttp
import os


async def download_repository(config_url, config_temp_folder, hash_list):
    url = config_url
    temp_folder = config_temp_folder
    filename = f'{url.split("/")[-1]}.zip'
    headers = {'Accept': 'application/zip'}

    async with aiohttp.ClientSession() as session:
        async with session.head(url, headers=headers) as response:
            response.raise_for_status()

            create_temp_folder(temp_folder)

            async with session.get(url, headers=headers) as download_response:
                await save_to_file(temp_folder, filename, download_response, hash_list)


def create_temp_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def rename(name, path):
    index = 1
    while True:
        newname = f"{name.split('.zip')[0]}({index}).zip"
        if not os.path.exists(f'{path}/{newname}'):
            break
        index += 1
    return newname


async def save_to_file(folder_path, filename, download_response, hash_list):
    check_file = os.path.join(folder_path, filename)
    if os.path.exists(check_file):
        filename = rename(filename, folder_path)

    with open(os.path.join(folder_path, filename), 'wb') as file:
        while True:
            chunk = await download_response.content.read(1024)
            if not chunk:
                break
            file.write(chunk)
        hash_list.append(filename)
        print(f'Файл {filename} сохранен по пути {folder_path}/')
