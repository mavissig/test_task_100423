import hashlib
from pathlib import Path


def hash_calculator(path, hash_list):
    for file in hash_list:
        hash_sum = get_hash(f'{path}/{file}')
        hash_log_text = f"Hash {file} = {hash_sum};"
        with open(f'{path}/hash_log.txt', 'a') as wb:
            wb.write(f'{hash_log_text}\n')
        print(hash_log_text)


def get_hash(filename, algorithm='sha256'):
    obj_hash = hashlib.new(algorithm)
    with open(filename, 'rb') as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            obj_hash.update(data)
    return obj_hash.hexdigest()
