#!/usr/bin/env bash

# Grab ini value from config.ini
# https://intellipaat.com/community/4017/how-do-i-grab-an-ini-value-within-a-shell-script
venv_activate_path=$(awk -F "=" '/venv_activate_path/ {print $2}' config.ini)
stats_updater_path=$(awk -F "=" '/stats_updater_path/ {print $2}' config.ini)

# Activate virtual environment
source $venv_activate_path

# Run Python code.
python $stats_updater_path

# Perform cleanup.
deactivate
read -p "Press enter to continue"