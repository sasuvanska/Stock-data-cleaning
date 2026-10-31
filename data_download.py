import yfinance as yf
from pathlib import Path

def main():
    """Download Disney stock price data"""

    start_date = "2010-01-01"
    end_date = "2015-12-31"
    ticker = "DIS"

    data = yf.download(ticker, start=start_date, end=end_date, actions=True)
    data.to_csv("/Users/sasuvanska/Library/CloudStorage/OneDrive-Personal/Project/Code/Project 1/dis_data.csv")

    data = open("DIS_data", mode="w")
    
    if data != None:
        print("Data downloaded")
    
    data.close

if __name__=="__main__":
    main()