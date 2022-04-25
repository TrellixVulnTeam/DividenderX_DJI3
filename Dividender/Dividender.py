import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def getDividendQuarter(Price, DivdendPerShare, Quarters, Ticker="UnderlyingAsset"):
    equityHistory = []
    newerReturn = []
    normalDiviReturn = DivdendPerShare/ Price
    equity = Price
    for i in range(Quarters):
        temp = equity * normalDiviReturn
        # print(temp)
        equity += temp
        # print(equity)
        #print(str(i+1),"equity ---> ", equity, "and", "temp ---->", temp)
        equityHistory.append(equity)
        newerReturn.append(temp)
    df = pd.DataFrame(equityHistory, columns=["EquityHistory"])
    df['EquityHistory'].plot(title=Ticker)
    plt.xlabel("Quarters")
    plt.ylabel("USD Growth")
    plt.show()

    return equityHistory
def getDividendMonthly(Price, DivdendPerShare, Month, Ticker="UnderlyingAsset"):
    equityHistory = []
    newerReturn = []
    normalDiviReturn = DivdendPerShare/ Price
    equity = Price
    for i in range(Month):
        temp = equity * normalDiviReturn
        # print(temp)cls
        equity += temp
        # print(equity)
        #print(str(i+1),"equity ---> ", equity, "and", "temp ---->", temp)
        equityHistory.append(equity)
        newerReturn.append(temp)
    df = pd.DataFrame(equityHistory, columns=["EquityHistory"])
    df['EquityHistory'].plot(title=str(Ticker))
    plt.xlabel("Months")
    plt.ylabel("USD Growth")
    plt.show()
    return equityHistory


#getDividendMonthly(12,0.1,8,"PFLT")


