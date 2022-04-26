import pandas_datareader.data as web
import pandas as pd
import datetime as dt

def scrape_finance_data(ticker, start_date, end_date):
    '''
    Scrape a company's stock for specified time period
    from Yahoo Finance

    ticker: (str) the ticker of a publicly traded company
    start_date: (datetime) start date of scraping
    end_date: (datetime) end date of scraping
    '''

    df = web.DataReader(ticker, 'yahoo', start = start_date, end = end_date)
    file_name = '{}_data.csv'

    return df.to_csv(file_name.format(ticker), index = True)