import pandas as pd
import matplotlib.pyplot as plt

msft = pd.read_csv("MSFT.csv", parse_dates=["Date"], index_col="Date")
msft.info()

msft.head()

msft.resample("M").last()

plt.style.use("seaborn")
plt.figure(figsize=(12,9))
plt.plot(msft.index, msft.Open, label="open", color="r")
plt.plot(msft.index, msft.High, label="high", color="b")
plt.legend(loc="best", fontsize=15)
plt.show()

msft.index
# msft.Volume.plot(kind="hist")
