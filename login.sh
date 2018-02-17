#!/bin/bash

tmux new-session -A -s schedule;
# change path to whatever directory scheduler.py is in
python3 /home/pi/redditbot/scheduler.py;
tmux kill-session;

