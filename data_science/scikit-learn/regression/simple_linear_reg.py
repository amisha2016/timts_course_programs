from sklearn import linear_model
import csv
import numpy as np

def sklearn_linear_reg(dataset):
    x=np.array([row[0] for row in dataset]) # Take first column of dataset as x and convert list to NumPy array
    y=np.array([row[1] for row in dataset])
    x=x[:,np.newaxis] # Convert 1-D array to 2-D array or increase dimension of array by 1
    y=y[:,np.newaxis] # as fit function take 2-D array to perform inner operations may be dot product
    reg=linear_model.LinearRegression()
    reg.fit(x,y) # Fit linear model to find slope and intercept
    slope=reg.coef_[0] # return slope of a line
    intercept=reg.intercept_ # return intercept of line
    print("slope=",slope, "intercept=",intercept)

if __name__=="__main__":

    with open('../../../dataset/AutoInsurSweden.csv', 'r') as f:
      reader = csv.reader(f) # read data from file and save it to reader variable in string form
      data = list(reader)
      dataset=data[:5] # retrieve first five rows of list data 
      dataset=[[float(col) for col in row] for row in dataset] # convert data from string to numeric(float)
      sklearn_linear_reg(dataset) # calling funtion

