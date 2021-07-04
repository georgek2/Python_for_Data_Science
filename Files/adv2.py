# Making directories

import os
from pathlib import Path 

# os.mkdir('First')

# p = Path('SEcond')
# p.mkdir()

# If the Folder exists, 
# AN error is raised

# os.mkdir('First')

# Avoiding the error
# try:
#     os.mkdir('First')
# except FileExistsError as error:
#     print(error)

# try:
#     p.mkdir()
#     # p = Path('SEcond')
# except FileExistsError as error:
#     print(error)

# ALternatively, ignore the error
# Code below will not return the error

# p = Path('SEcond')
# p.mkdir(exist_ok=True)

# MAking multiple directories
# try:
#    os.makedirs('Luke/Jane/Love')
# except:
#     print('Zimeisha') 

# p = Path('I/Love/That/This')
# p.mkdir(parents=True)

# with open('luke.txt', 'a') as f:
#     f.write('I made it nigga....')
#     f.write('\nYooooh!!!!!...')

basepath = Path('./')

# entries = os.scandir('./')
# Better
# with os.scandir('./') as entries:
#     for entry in entries:
#         print(entry.name)

# Or

# entries = basepath.iterdir()
# for entry in entries:
#     if entry.is_dir():
#         print(entry.name)

# files = (entry for entry in basepath.iterdir() if entry.is_file())

# for file in files:
#     print(file)

# WHen Files were last modified
# # os
# with os.scandir('./') as dir_contents:
#     for entry in dir_contents:
#         info = entry.stat()
#         print(info.st_mtime)

# # pathlib.Path
# print('*' * 30)
# cur_dir = Path('./')
# for entry in cur_dir.iterdir():
#     info = entry.stat()
#     print(info.st_mtime)

# Converting the modification time from seconds to a date

# from datetime import datetime
# def convert_time(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     converted_d = d.strftime('%d %m %Y')

#     return converted_d

# def get_files():
#     entries = os.scandir('./')
#     for entry in entries:
#         if entry.is_file():
#             info = entry.stat()
#             timestamp = info.st_mtime
#             print(f'{entry.name} \t\t Last modified: {convert_time(timestamp)}')

# get_files()

# Making directories

p = Path('Boom')
# p.mkdir()

# os.mkdir('Chaka')

# If dir exists >> erro
# To avoid the error = Catch it
try:
    p.mkdir()
    # os.mkdir('Chaka')
except:
    print('Directory already Exists')

# Or simply ignore it
p.mkdir(exist_ok=True)






