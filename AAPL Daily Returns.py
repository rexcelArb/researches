import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker


df = pd.read_csv(r"C:\Users\Rexcel Abila\Downloads\AAPL.csv")


df["Date"] = pd.to_datetime(df["Date"])


df.set_index("Date", inplace=True)


df["Returns"] = df["Close"].pct_change()


plt.plot(df.index, df["Returns"])
plt.xlabel("Date")
plt.ylabel("Returns")
plt.title("Daily Returns of AAPL")
plt.show()


fig, ax = plt.subplots()


candlestick_ohlc(ax, df[["Open", "High", "Low", "Close"]].values, width=0.6, colorup="green", colordown="red")


