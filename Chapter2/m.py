# -*- coding: utf-8 -*-
# lesson 2.4
import os
paths = list()
for current_path, dirs, files in os.walk("main"):
	for f in files:
		if f[-3:] == ".py":
			paths.append(current_path)
			break

with open("file.txt", "w") as f:
	for path in paths:
		f.write(path + "\n")