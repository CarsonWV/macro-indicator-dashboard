![main_logo](https://github.com/CarsonWV/macro-indicator-dashboard/raw/main/assets/MacroDash-logo-white.png)

# Summary
A GitHub Pages site that hosts live-feeds of arbitrary macroeconomic indicators. 
Website made of pure HTML, CSS. Stats updated daily by a python script running on a Raspberry Pi 3B.

# Install
* Install python dependencies: [fredapi](https://github.com/mortada/fredapi) [chart-studio](https://pypi.org/project/chart-studio/)
* Clone the repository.

# Setup
Configure config.ini to include:
* API Keys: [FRED API](https://research.stlouisfed.org/docs/api/api_key.html), [Plotly API](https://community.plotly.com/t/how-could-i-get-my-api-key/3088)
* Path to "activate" file in virtual environment.
* Path to stats_updater.py
* If necessary, use [dos2unix](https://linux.die.net/man/1/dos2unix) to reset config and script file.

# Usage
* Schedule script.sh to run as often as you need it using Chron
![usage_picture]((https://github.com/CarsonWV/macro-indicator-dashboard/raw/main/assets/screenshot-cropped.png)
