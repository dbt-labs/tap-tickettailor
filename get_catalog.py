#!/usr/bin/env python
import sys
import json
import subprocess
from collections import OrderedDict


output = subprocess.check_output(['tap-tickettailor', '-d', '-c', 'config.json'])
schema = json.loads(output.decode("utf-8"), object_pairs_hook=OrderedDict)
streams = schema["streams"]
for s in streams:
    s["schema"]["selected"] = True
    s["metadata"][0]["metadata"]["selected"] = True

json.dump(schema, fp=sys.stdout, indent=2)

