#!/usr/bin/env python3

with open("devops_notes.txt", "w") as file:
   file.write("Day 2: Python can read and write files.\n")

with open("devops_notes.txt", "r") as file:
   content = file.read()
   print("File content:")
   print(content)
