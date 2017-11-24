# -*- coding: utf-8 -*-
# Immutable and mutable objects on CPython
ans = 0
t = []
for obj in objects: # доступная переменная objects
    if obj not in t:
        t.append(obj)
        ans += 1
print(ans)