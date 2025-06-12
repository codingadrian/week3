#!/usr/bin/venv python3


import os

if os.path.exists("src/"):
   print(f"The directory already exists")
if not os.path.exists("src/"):
   print(f"Do you want me to create it?")
   exit: 1
