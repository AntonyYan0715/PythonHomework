import math
import os
import random
import re
import sys
import pandas as pd
import numpy as np
def case1(financial_data):
    # Print First 5 rows of MSFT
    # Print Last 5 rows of MSFT
    print(financial_data.head(5))
    print(financial_data.tail(5))

def case2(financial_data):
    #Resample to monthly data mean
    #Display the first 5 rows
    #financial_data.set_index('Date', inplace=True)
    financial_data.index = pd.to_datetime(financial_data.index)
    df = financial_data.resample('M').mean()
    # df = financial_data.resample('M').agg({'High':'max', 'Low': 'min', 'Open':'first', 'Close':'last', 'Volume':'sum', 'Adj Close':'last'})
    print(df.head(5))

def case3(financial_data):
    # Create a variable daily_close and copy Adj Close from financial_data
    # Print first 20 daily returns
    daily_close = pd.DataFrame(financial_data['Adj Close'])
    daily_close['Adj Close'] = daily_close['Adj Close'].pct_change()
    print(daily_close.head(20))

def case4(financial_data):
    # Calculate the cumulative daily returns
    # day1 : return1  cumulative reuturn : (1+return1)-1
    # day2 : return2  cumulative reuturn : (1+return1)*(1+return2)-1
    # Print first 20 rows
    daily_close = pd.DataFrame(financial_data['Adj Close'])
    daily_close['Adj Close'] = daily_close['Adj Close'].pct_change()
    daily_close['Adj Close'] = (daily_close['Adj Close'] + 1).cumprod() - 1
    print(daily_close.head(20))

def case5(financial_data):
    # Isolate the adjusted closing prices and store it in a variable
    # Calculate the moving average for a window of 20
    # Display the last 20 moving average number
    daily_close = pd.DataFrame(financial_data['Adj Close'])
    daily_close['Adj Close'] = daily_close['Adj Close'].rolling(20).mean()
    print(daily_close.tail(20))


def case6(financial_data):
    # Calculate the volatility for a period of 100 don't forget to multiply by square root
    # don't forget that you need to use pct_change
    # Print last 20 rows
    daily_close = pd.DataFrame(financial_data['Adj Close'])
    daily_close['Adj Close'] = daily_close['Adj Close'].pct_change().rolling(100).std() * (100**0.5)
    print(daily_close.tail(20))

