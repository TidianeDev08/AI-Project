import numpy as np

def initialisation(n_pixels):
    W = np.random.randn(n_pixels, 1)
    b = 0
    return W, b

def model(X, W, b):
    Z = np.dot(W.T, X) + b  
    A = 1 / (1 + np.exp(-Z))
    return A