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
pattern = r"a[ab]+a"
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))