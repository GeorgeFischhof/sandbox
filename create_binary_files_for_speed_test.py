from os import makedirs
from random import getrandbits
from random import randint
import time
import uuid

files_to_create = [
    {"folder_name": "small_files", "min_bytes": 10, "max_bytes": 100, "number_of_files": 10_000},
    {"folder_name": "medium_files", "min_bytes": 50_000_000, "max_bytes": 500_000_000, "number_of_files": 10},
    {"folder_name": "big_file", "min_bytes": 1_000_000_000, "max_bytes": 1_000_000_000, "number_of_files": 5},
]

start = time.time()

for folder in files_to_create:
    makedirs(folder["folder_name"], exist_ok=True)
    for file_to_create in range(folder["number_of_files"]):
        chunk = bytearray(getrandbits(8) for index in range(randint(folder["min_bytes"], folder["max_bytes"])))
        with open(f"{folder['folder_name']}/{uuid.uuid4().hex}", "wb") as output:
            output.write(chunk)

stop = time.time()
print(f"duration {int(stop - start)} seconds")
