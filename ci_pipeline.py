#!/usr/bin/env python3

import os
from datetime import datetime

# Simulate validation

required_files = ["README.md", ".github/workflows/ci.yml"]
missing = [f for f in required_files if not os.path.isfile(f)]

log_file = "build.log"
with open(log_file, "w") as log:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.write(f"[{timestamp}] Build started\n")
    if missing:
        log.write("X Missing files:\n")
        for f in missing:
            log.write(f" - {f}\n")
        exit(1)
    else:
        log.write("All required files found\n")

print("CI Pipeline completed successfully")