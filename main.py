import datetime
import pytz
import pandas as pd
import MetaTrader5 as mt5
import numpy as np

# Define the time frames that will be used for importing data from MetaTrader5
frame_M15 = mt5.TIMEFRAME_M15 # 15 minute timeframe
frame_M30 = mt5.TIMEFRAME_M30 # 30 minute timeframe
frame_H1 = mt5.TIMEFRAME_H1 # Hourly timeframe
frame_D1 = mt5.TIMEFRAME_D1 # Daily timeframe
frame_W1 = mt5.TIMEFRAME_W1 # Weekly timeframe
frame_M1 = mt5.TIMEFRAME_MN1 # Monthly timeframe
frame_H4 = mt5.TIMEFRAME_H4 # 4 hour timeframe

now = datetime.datetime.now()

def get_quotes(time_frame, year = 2005, month = 1, day = 1, asset = "EURUSD"):
	if not mt5.initialize():
		print("Initialize() failed, error code = ", mt5.last_error())
		quit()

	timezone = pytz.timezone("Europe/Paris")
	time_from = datetime.datetime(year, month, day, tzinfo = timezone)
	time_to = datetime.datetime.now(timezone) + datetime.timedelta(days = 1)
	rates = mt5.copy_rates_range(asset, time_frame, time_from, time_to)
	rates_frame = pd.DataFrame(rates)
	return rates_frame

def mass_import(asset, time_frame):
	if time_frame == 'H1':
		data = get_quotes(frame_H1, 2013, 1, 1, asset = assets[asset])
		data = data.iloc[:, 1:5].values
		data = data.round(decimals = 5)

	if time_frame == 'D1':
		data = get_quotes(frame_D1, 2000, 1, 1, asset = assets[asset])
		data = data.iloc[:, 1:5].values
		data = data.round(decimals = 5)

	return data

