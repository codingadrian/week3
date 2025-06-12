#!/usr/bin/env python3
import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
dirname = f"build_{timestamp}"

os.makedirs(dirname, exist_ok=True)
print(f"Created build directory: {dirname}")

with open(os.path.join(dirname, "status.txt"), "w") as f:
  f.write("Build directory initialized\n")
