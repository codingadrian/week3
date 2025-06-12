#!/usr/bin/env python3

import os

author = os.getenv("AUTHOR", "Anonymous")
print(f"Script run by: {author}")
