import csv
import numpy as np
import pandas as pd
from math import sqrt

def rmse_metric(actual,predicted):
    sum_err=0.0
    for i in range(len(actual)):
        difference=pd.to_numeric(actual[i])-pd.to_numeric(predicted[i])
        abs_diff=difference**2
        sum_err+=abs_diff
    avg_err=sum_err/len(actual)
    rmse=sqrt(avg_err)
    return rmse

if __name__=="__main__":

    with open('dataset/AutoInsurSweden.csv', 'r') as f:
      reader = csv.reader(f)
      data = np.array(list(reader))

    actual=data[:10,[0]]
    predicted=data[10:20,[1]]
    rmse_metric(actual,predicted)

