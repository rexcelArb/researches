
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv(r"C:\Users\Rexcel Abila\Downloads\AAPL.csv")

a['money_inflow'] = a['Close'] * a['Volume']

dates = np.array(a['Date'])
money_inflow = np.array(a['money_inflow'])

fig, ax = plt.subplots()

ax.plot(dates, money_inflow)

ax.set_xlabel('Date')

ax.set_ylabel('Money Inflow')

plt.show()
