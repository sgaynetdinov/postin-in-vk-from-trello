#!/bin/bash
ACTIVATE_SCRIPT=/path/to/environment/activate
RUN_SCRIPT=/path/to/project/main.py
source $ACTIVATE_SCRIPT
python $RUN_SCRIPT
echo "done"