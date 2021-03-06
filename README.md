![main_logo](https://github.com/CarsonWV/macro-indicator-dashboard/raw/main/assets/MacroDash-bg.png)

# Summary
MacroDash is a GitHub Pages site that hosts descriptions and live-feeds of arbitrary macroeconomic indicators.
This particular iteration displays the following:
* USA Real Gross Domestic Product
* USA Consumer Price Index for All Urban Consumers
* USA 10-Year Break-Even Inflation Rate

Website built using pure HTML, CSS. Indicators are updated daily by a Python script running on a Raspberry Pi 3B.

# Install
* Clone this repository.
* Enable [Github Pages](https://guides.github.com/features/pages/) from Settings.
* Install python dependencies, preferably to a virtual environment:
  * [fredapi](https://github.com/mortada/fredapi)
  * [chart-studio](https://pypi.org/project/chart-studio/)
```
$ pip install -r requirements.txt
```

# Setup
Configure config.ini to include:
* API Keys for
  * [FRED](https://research.stlouisfed.org/docs/api/api_key.html)
  * [plotly](https://community.plotly.com/t/how-could-i-get-my-api-key/3088)
* [Absolute paths](https://www.linux.com/training-tutorials/absolute-path-vs-relative-path-linuxunix/) for:
  * Python interpreter OR [virtual environment](https://docs.python.org/3/library/venv.html) 'activate' file.
  * stats_updater.py (located in scripts folder).
> [dos2unix](https://linux.die.net/man/1/dos2unix) might be necessary to configure config.ini and script.sh for unix.

# Usage
![usage_picture](https://github.com/CarsonWV/macro-indicator-dashboard/raw/main/assets/screenshot-cropped.png)
* Scheduling performed on unix by [Cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md).
* To schedule, create a Cron entry for 'script.sh' once config.ini has been set up. All errors logged with dates and times to error_log.txt for easy management.
