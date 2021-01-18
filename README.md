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
  * [FRED API](https://research.stlouisfed.org/docs/api/api_key.html)
  * [Plotly API](https://community.plotly.com/t/how-could-i-get-my-api-key/3088)
* [Absolute paths](https://www.linux.com/training-tutorials/absolute-path-vs-relative-path-linuxunix/) for:
  * Python interpreter OR [virtual environment](https://docs.python.org/3/library/venv.html) ACTIVATE file.
  * stats_updater.py (located in stats_updater folder).
> [dos2unix](https://linux.die.net/man/1/dos2unix) might be necessary to configure config.ini and script.sh for unix.

# Usage
* Schedule script.sh to run as often as you need it using Chron  

![usage_picture](https://github.com/CarsonWV/macro-indicator-dashboard/raw/main/assets/screenshot-cropped.png)
