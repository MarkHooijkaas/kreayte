#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

import kreayte #.Deployment

data={
    "APP": "testapp"
}

kreayte.deployment(data)
