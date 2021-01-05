#!/bin/bash

LOG_FILE="sync-client.log"

cd $(dirname $0)
exec &>> $LOG_FILE
. venv/bin/activate
python sync-client.py
