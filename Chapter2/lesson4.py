# -*- coding: utf-8 -*-
# lesson 2.4: work with file's system and files
'''
f = open("test.txt", 'r')
for line in f:
	line = line.rstrip()
	print(line)
f.close()
'''
'''
file = open("test1.txt", "w")

lines = ["line1", "line2", "line3"]
contents = "\n".join(lines)
file.write(contents)

file.close()
'''
import os
import os.path
import shutil
'''
print(os.getcwd())
print(os.listdir("C:\\")) 
print(os.path.exists("fib.py"))
print(os.path.exists("E:\Python\stepik-Python\Chapter1\lesson1.py"))
print(os.path.isfile(os.getcwd()))
print(os.path.isfile("fib.py"))
print(os.path.isdir(os.getcwd()))
print(os.path.isdir("fib.py"))
print(os.path.abspath("lesson4.py"))
os.chdir("E:\Python\stepik-Python")
print(os.getcwd())
print('\n')''''''
for current_dir, dirs, files in os.walk("E:\\"):
	print(current_dir, dirs, files)'''
'''
shutil.copy("tests/test1.txt", "tests/text2.txt")
for current_dir, dirs, files in os.walk("."):
	print(current_dir, dirs, files)
'''
'''
shutil.copytree("tests", "tests\\tests1")
for current_dir, dirs, files in os.walk("."):
	print(current_dir, dirs, files)
'''
