#!/bin/bash
#~/redditbot/login.sh

tmux new-session -A -s schedule;
python3 /home/pi/redditbot/scheduler/scheduler.py;
tmux kill-session;

