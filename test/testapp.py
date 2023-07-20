#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

import kreayte
import yaml

with open('test/app-def.yaml', 'r') as file:
    data = yaml.safe_load(file)

kreayte.deployment(data)
