#!/bin/bash

source ~/.virtualenvs/emojitex.sty/bin/activate
cd "$(dirname "$0")"
python main.py
