# Created by Carson Weaver on 2020-01-08 for Economic Indicator Project

# Program Goals:
# 1. Updates plotly-hosted charts.
# 2. Documents errors.
# 3. Retrieves variables from config file.

from datetime import datetime
from time import sleep
from configparser import ConfigParser
from fredapi import Fred
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.express as px

# Config variables.
config = ConfigParser()
config.read('config.ini')
fred_api_key = config['FRED']['fred_api_key']
plotly_api_key = config['PLOTLY']['plotly_api_key']
plotly_username = config['PLOTLY']['plotly_username']
request_pause_seconds = int(config['PROGRAM']['request_pause_seconds'])

if fred_api_key == 'None' or plotly_username == 'None' or plotly_api_key == 'None':
	raise ValueError("Your config.ini file is missing one or more usernames/apikeys.")

# Essential program variables:
global run_without_errors
run_without_errors = True
data_dict = {}

def print_and_pause(message, name):
	print(f"{message}: {name}")
	sleep(request_pause_seconds)

def cleanup(message): # Log any errors to their designated text file.
	global run_without_errors
	if run_without_errors:
		run_without_errors = False
	print(message)
	with open('error_log.txt', 'a+') as error_log:
		now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		error_log.write('\n' + str(now) + ' - ' + str(message))

try:
	# Retreive the FIRST time series (FRED GDP).
	fred = Fred(fred_api_key) # Login.
	name = "Real Gross Domestic Product"
	data = fred.get_series(series_id="A191RL1Q225SBEA", observation_start="2010-01-01", observation_end="2012-01-01")
	data_dict[name] = data
	print_and_pause('Saved', name)
except:
	cleanup(f"Error retreiving and/or parsing series: {name}.")

try:
	# Retreive the SECOND time series (FRED CPI).	
	fred = Fred(fred_api_key) # Login.
	name = "Consumer Price Index for All Urban Consumers"
	data = fred.get_series(series_id="CPIAUCSL", observation_start="2007-01-01", observation_end="2012-01-01")
	data_dict[name] = data
	print_and_pause('Saved', name)
except:
	cleanup(f"Error retreiving and/or parsing series: {name}.")

try:
	# Retreive the THIRD time series (FRED 10-YEAR INFLATION).	
	fred = Fred(fred_api_key) # Login.
	name = "10-Year Breakeven Inflation Rate"
	data = fred.get_series(series_id="T10YIE", observation_start="2006-07-01", observation_end="2012-01-01")
	data_dict[name] = data
	print_and_pause('Saved', name)
except:
	cleanup(f"Error retreiving and/or parsing series: {name}.")

try:
	# Log into the Plotly account.
	tls.set_credentials_file(plotly_username, plotly_api_key)
	print_and_pause("Logging into", "Plotly API")
except:
	cleanup("Error logging into plotly.")

try:
	# Submit each item to plotly cloud.
	for name, data in data_dict.items():
		fig = px.line(data, title=name) # Plot item.
		py.plot(fig, filename=name, auto_open=False) # Ship item off to the Plotly API.
		print_and_pause('Shipped', name)
except:
	cleanup("Error shipping off charts.")

if run_without_errors:
	cleanup("Done")