import pandas as pd
from pandas import DataFrame
from sklearn import linear_model

stock_market = pd.read_csv(r'../../../dataset/economy.csv') #return dataframe
#data_frame = DataFrame(stock_market,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price'])
X=stock_market[['Interest_Rate','Unemployment_Rate']]
Y=stock_market['Stock_Index_Price']
regr=linear_model.LinearRegression()
regr.fit(X,Y)
print(regr.coef_)
