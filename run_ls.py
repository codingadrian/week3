#!/usr/bin/env python3

import subprocess

result = subprocess.run(["ls", "-lah"], capture_output=True, text=True)
print(result.stdout)

