#!/bin/bash

python3 -m venv stitch
source stitch/bin/activate
pip install target-stitch
deactivate

python3 -m venv tap
source tap/bin/activate
pip install -e .
deactivate

### Load configuration
echo "$STITCH_CONFIG" > persist.json
echo "$TAP_CONFIG" > config.json
echo "$CATALOG" > catalog.json

### Run the tap
./tap/bin/tap-tickettailor -c config.json --catalog catalog.json | ./stitch/bin/target-stitch -c persist.json
