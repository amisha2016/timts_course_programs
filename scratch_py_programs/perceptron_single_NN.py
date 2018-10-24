'''
It is the Perceptron supervised learning algorithm with single hidden layer.
This program will calculate weights and bias accurately and using that will predict output for corresponding input
For theory part go to the link https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
'''

import numpy as np

# It is the activation function sigma(xw+b)
def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

# It will calculate derivatve of sigmoid function
def sigmoid_derivative(x):
    return x * (1.0 - x)

#This class will train the neurons
class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) #Assume 4 neurons of hidden layer
        self.weights2   = np.random.rand(4,1) #generate an array of 4*1 dimension with random values                
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1)) #Assume value of bias=0 
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1 # update the weights associated with input and hidden layer
        self.weights2 += d_weights2 # update the weights associated with hidden and output layer

'''
Input Training set(X): Here each row of an array X is an instance of training set and the number of elements in each row is the number of features of an instance. Each feature is described by single input neuron i.e if 3 features it means 3 input neurons.

Output Training Set(y): Each instance of a training set is mapped to a single output neuron. i.e. for input [0,0,1] the output is [0]. Similarly for other training instances.
'''

if __name__ == "__main__":
    X = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
    y = np.array([[0],[1],[1],[0]])
    nn = NeuralNetwork(X,y)

    for i in range(1500): #will run functions 1500 times for good approximations
        nn.feedforward()
        nn.backprop()

    print(nn.output)
