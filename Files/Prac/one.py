import os
import pathlib
import glob 

# try:
#     os.makedirs('First/sub_two')
# except:
#     print('Folder already in place')

# try:
#     f = open('File.txt', 'a')
#     f.write('Having to do it the hard way \nBut it pays off in the end')
# except:
#     print('Non-existent file name')

# Replacing content in the file
# f = open('File.txt', 'w')
# f.write('Hahaaa!! Sucker..&')
# open('again.txt', 'x')

# entries = os.listdir('./')
# print(entries)

# p = pathlib.Path('./')
# entries = p.iterdir() # Iterator
# for entry in entries:
#     if entry.is_dir():
#         print(entry)

# open('great.js', 'x')
# f = open('File.txt', 'r')
# print(f.read())

# f = open('First/again.txt', 'a')
# f.write('Hae there mudu....##\n')
# f.close()

# f = open('First/again.txt', 'r')
# print(f.read())

# with open('First/again.txt', 'w') as f:
#     f.write('Massacared motherfucker')

# with open('First/again.txt', 'r') as f:
#     print(f.read())

# os.makedirs('Second/you.txt')

# open('you.txt', 'x')
# os.remove('you.txt')
p = pathlib.Path('./')
# for entry in p.iterdir():
#     if entry.is_file():
#         print(entry.name)

# List comprehension 
# files = [entry for entry in p.iterdir() if entry.is_file()]
# for item in files:
#     print(item.name)

import fnmatch

# print(glob.glob('./'))
# Matching file patterns

# String methods
# for item in os.listdir('./'):
#     if item.endswith('.js'):
#         print(item)

# fnmatch
p = pathlib.Path('./')
for item in p.iterdir():
    if fnmatch.fnmatch(item, '*.txt'):
        print(item)

# File attributes

# LAst modified
# for entry in os.scandir('./'):
#     info = entry.stat()
#     print(info.st_mtime)
















