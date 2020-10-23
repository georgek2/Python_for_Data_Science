# Using with open

# with open('luke.txt', 'r') as f:
#     data = f.read()
#     print(data)

# with open('banda.txt', 'a') as f:
#     f.write('\nJane has one there...')

# with open('banda.txt', 'r') as f:
#     data = f.read()
#     print(data)

# Working with subdirectories...
import os
from pathlib import Path

# entries = os.scandir('Had_it/')
# print(entries)

# One way
# with os.scandir('./') as entries:
#     for entry in entries:
#         print(entry.name)

# # Two
# entries = Path('./')

# for entry in entries.iterdir():
#     print(entry.name)

# with os.scandir('./Had_it') as entries:
#     for entry in entries:
#         if entry.is_dir():
#             print(entry.name)

# basepath = Path('./')

# files = basepath.iterdir()
# for item in files:
#     if item.is_file():
#         print(item.name)

# List comprehension
# them = [item for item in basepath.iterdir() if item.is_file()]

# # print(them)

# for item in them:
#     print(item.name)

# Getting File Attributes

# with os.scandir('./') as dir_contents:
#     for entry in dir_contents:
#         info = entry.stat()
#         print(info.st_mtime)

# Pathlib.Path

# basepath = Path('./')
# for entry in basepath.iterdir():
#     info = entry.stat()
#     print(str(entry) + ' ' + str(info.st_mtime))

# Converting the seconds to data time

from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp) 
    formatted_date = d.strftime('%d-%b-%Y')
    return formatted_date

def get_files():
    basepath = Path('./')
    for entry in basepath.iterdir():
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last modified {convert_date(info.st_mtime)}')

print(get_files())