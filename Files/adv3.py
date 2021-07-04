import os
from pathlib import Path
# File Pattern Matching

# All .txt files
# for f_name in os.listdir('./'):
#     if f_name.endswith('.txt'):
#         print(f_name)

# open('adv_02_backup.txt', 'x')

# Matching file names that adhere to a given condition
import fnmatch
import glob

# Get all .txt files whose name start with 'adv' and end with 'backup'
# for f_name in os.listdir('./'):
#     if fnmatch.fnmatch(f_name, 'adv_01_*_backup.txt'):
#         print(f_name)

# print(glob.glob('*.js'))

# for name in glob.glob('*[0-9]*.txt'):
#     print(name)

# USing iglob to search through all sub directories as well
# print(glob.iglob('**/*.py', recursive=True))
# # This print returns an iterator

# # Looping through to get individual file names
# for f_name in glob.iglob('**/*.txt', recursive=True):
#     print(f_name)

# for item in  os.listdir('./'):
#     if fnmatch.fnmatch(item, 'adv_*_backup.txt'):
#         print(item)

# for item in os.listdir('./'):
#     if item.endswith('.txt'):
#         print(item)

# for item in glob.glob('*[0-9]*.txt'):
#     print(item)

# print(glob.glob('*[0-9]*.txt'))

# for item in glob.iglob('**/*.txt', recursive=True):
#     print(item)

# p = Path('Do/Good/Always')
# p.mkdir(parents=True, exist_ok=True)

p = Path('./')
entries = p.iterdir()

for entry in entries:
    if fnmatch.fnmatch(entry, '*.txt'):
        print(entry)








