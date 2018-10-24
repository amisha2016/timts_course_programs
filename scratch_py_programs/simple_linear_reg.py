import csv
import numpy as np
from rmse_metric import rmse_metric

def mean(values):
    return sum(values)/float(len(values))

def variance(values, mean):
    return sum([(i-mean)**2 for i in values])

def covariance(x, mean_x, y, mean_y):
    covar=0.0
    for i in range(len(x)):
        covar+=(x[i]-mean(x))*(y[i]-mean(y))
    return covar

def calc_coefficients(dataset):
    x=[row[0] for row in dataset]
    y=[row[1] for row in dataset]
    mean_x, mean_y=mean(x), mean(y)
    covar=covariance(x, mean_x, y, mean_y)
    slope=covar/variance(x, mean_x)
    constant=mean_y-slope*mean_x
    return[slope, constant]

def linear_regression(train,test):
    predictions=list()
    slope, constant=calc_coefficients(train)
    for row in test:
        y=constant+slope*row[0]
        predictions.append(y)
    return predictions

def eval_linear_reg(dataset,algorithm):
    predictions=algorithm(dataset,dataset)
    actual=[row[-1] for row in dataset]
    print ('predictions : ', predictions)
    rmse=rmse_metric(actual, predictions)
    print ('rmse: ', rmse)
    return rmse

if __name__=="__main__":

    with open('dataset/AutoInsurSweden.csv', 'r') as f:
      reader = csv.reader(f)
      data = list(reader)
      #dataset=data[:5]
      #dataset=[[float(col) for col in row] for row in dataset]
      dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
      print ('dataset: ', dataset)
      eval_linear_reg(dataset,linear_regression)
