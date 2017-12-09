# -*- coding: utf-8 -*-
# lesson 3.3: regular expressions in Python.

# raw lines
'''
x = "hello\nworld"
print(x)
x = r"hello\nworld"
print(x)
'''
import re

#print(re.match)
#print(re.search)
#print(re.findall)
#print(re.sub)
'''
pattern = r"abc"
string = "abscd"
match_object = re.match(pattern, string)
print(match_object)
string = "nabc"
match_object = re.search(pattern, string)
print(match_object)
'''
# [] -- можно указать множество подходящих символов
# . ^ * + ? { } [ ] \ | ( ) -- метасимволы
'''
pattern = r"a[abc]c"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
'''
'''
pattern = r"english\?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)
'''
'''
pattern = r"a\wc"
string = "abc, acc, aac, adc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r"a[^a-d]c"
string = "aBc, a.c, aac, a4c"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
'''
'''
pattern = r"ab*c"
string = "ac, abc, abbc, abbbc, abbbbbbc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r"ab+c"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r"ab?c"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r"ab{3}c"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
'''
'''
pattern = r"a[ab]+?b"
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))
'''
'''
pattern = r"(test|text){2}"
string = "testtest, texttext, test, text, texttesttexttest"
match = re.match(pattern, string)
findall = re.findall(pattern, string)
print(match)
print(findall)
'''
'''
pattern = r"((abc)|(test|text)*)"
string = "testtext"
match = re.match(pattern, string)
print(match)
print(match.groups())
print(re.findall(pattern, string))
print(re.search(pattern, string))
'''
'''
pattern = r"Hello (abc|test)"
string = "Hello abc"
match = re.match(pattern, string)
print(match)
print(match.group(0))
print(match.group(1))
'''
'''
pattern = r"(\w+)-\1"
string = "test-text"
match = re.match(pattern, string)
print(match)
'''
'''
pattern = r"((\w+)-\2)"
string = "test-test chow-chow"
duplicates = re.findall(pattern,1 string)
print(duplicates)
'''
'''
x = re.match(r"(tex)+?t", "TEXT", re.IGNORECASE | re.DEBUG)
print(x)
'''
'''
import sys, re
inputs_strings = []

while 1:
	try:
		inputs_strings.append(sys.stdin.readline().strip())
	except KeyboardInterrupt:
		break

pattern = r".*(cat)+.*(cat)+.*"
for string in inputs_strings:
	if not re.match(pattern, string) == None:
		print(string)
'''
'''
import sys, re
inputs_strings = []

while 1:
	try:
		inputs_strings.append(sys.stdin.readline().strip())
	except KeyboardInterrupt:
		break

pattern = r"\b(\w+)\1\b"
for string in inputs_strings:
	if re.search(pattern, string):
		print(string)
'''
'''
import sys, re
inputs_strings = []

while 1:
	try:
		inputs_strings.append(sys.stdin.readline().strip())
	except KeyboardInterrupt:
		break

def isthreedivision(line):
	count01 = 0
	count10 = 0
	if len(line) % 2 == 1:
		line = "0" + line
	nums = re.findall(r"(\d\d)", line)
	
	for num in nums:
		if num == "01": count01 += 1
		if num == "10": count10 += 1
	return (count01 - count10) % 3 == 0

pattern = r"\b(\w+)\1\b"
for line in inputs_strings:
	if isthreedivision(line.rstrip()):
		print(line.rstrip())
'''