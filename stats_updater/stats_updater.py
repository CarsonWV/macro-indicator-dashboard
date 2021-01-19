# Created by Carson Weaver on 2020-01-08 for Economic Indicator Project

# Program Goals:
# 1. Updates plotly-hosted charts.
# 2. Documents errors.
# 3. Retrieves variables from config file.

#################### IMPORTS ####################

from datetime import datetime
from time import sleep
from configparser import ConfigParser
from fredapi import Fred
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.express as px
import pandas as pd
import numpy as np


#################### CONFIG ####################

# Get config variables.
config = ConfigParser()
config.read('PRIVATEconfig.ini')
fred_api_key = config['FRED']['fred_api_key']
plotly_api_key = config['PLOTLY']['plotly_api_key']
plotly_username = config['PLOTLY']['plotly_username']
request_pause_seconds = int(config['PROGRAM']['request_pause_seconds'])

# Throw error if one or more doesn't exist.
if fred_api_key == 'None' or plotly_username == 'None' or plotly_api_key == 'None':
	raise ValueError("Your config.ini file is missing one or more usernames/apikeys.")

# Define essential program variables:
global run_without_errors
run_without_errors = True
charts = []


#################### HELPER FUNCTIONS ####################

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

def format_series(data, ident): # Turn the response series into a pandas dataframe.
	plot_series = pd.DataFrame(index=range(len(data.index)))
	plot_series[ident["x_axis"]] = data.index
	plot_series[ident["y_axis"]] = list(data)
	return plot_series


#################### GET DATA ####################
# Duplicated so that APIs can be swapped using minimal changes to an individual code block.

# Retreive the FIRST time series (FRED GDP).
meta_info = {"chart_name":"Real Gross Domestic Product","x_axis":"Date", "y_axis":"GDP"}
try:
	fred = Fred(fred_api_key) # Login.
	data = fred.get_series(series_id="A191RL1Q225SBEA", observation_start="2010-01-01", observation_end="2012-01-01")
	meta_info["data"] = format_series(data, meta_info)
	charts.append(meta_info)
	print_and_pause('Saved', meta_info["chart_name"])
except:
	cleanup(f"Error retreiving and/or parsing series: {meta_info['chart_name']}.")

# Retreive the SECOND time series (FRED CPI).	
meta_info = {"chart_name":"Consumer Price Index for All Urban Consumers","x_axis":"Date", "y_axis":"CPI"}
try:
	fred = Fred(fred_api_key) # Login.
	data = fred.get_series(series_id="CPIAUCSL", observation_start="2007-01-01", observation_end="2012-01-01")
	meta_info["data"] = format_series(data, meta_info)
	charts.append(meta_info)
	print_and_pause('Saved', meta_info["chart_name"])
except:
	cleanup(f"Error retreiving and/or parsing series: {meta_info['chart_name']}.")

# Retreive the THIRD time series (FRED 10-YEAR INFLATION).
meta_info = {"chart_name":"10-Year Breakeven Inflation Rate","x_axis":"Date", "y_axis":"INF Rate"}
try:	
	fred = Fred(fred_api_key) # Login.
	data = fred.get_series(series_id="T10YIE", observation_start="2006-07-01", observation_end="2012-01-01")
	meta_info["data"] = format_series(data, meta_info)
	charts.append(meta_info)
	print_and_pause('Saved', meta_info["chart_name"])
except:
	cleanup(f"Error retreiving and/or parsing series: {meta_info['chart_name']}.")


#################### SHIP DATA ####################

# Log into the Plotly account.
try:
	tls.set_credentials_file(plotly_username, plotly_api_key)
	print_and_pause("Logging into", "Plotly API")
except:
	cleanup("Error logging into plotly.")

# Submit each item to plotly cloud.
for item in charts:
	df = item["data"]
	fig = px.line(df, x=item['x_axis'], y=item["y_axis"], title=item["chart_name"]) # Plot item.
	py.plot(fig, filename=item["chart_name"], auto_open=False) # Ship item off to the Plotly API.
	print_and_pause('Shipped', item["chart_name"])

# Confirmation of completion.
if run_without_errors:
	cleanup("Done")