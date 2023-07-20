#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

import kreayte
import yaml

with open('test/app-def.yaml', 'r') as file:
    data = yaml.safe_load(file)

kreayte.deployment(data)
