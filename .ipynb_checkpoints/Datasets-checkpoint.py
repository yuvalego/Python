import numpy as np
def create_linear_data(m: int, n: int):
    '''takes in m as the amount of samples and n as the amount of features. output: X - (m, n) matrix and y (1, m) row vector'''
    X = np.random.rand(m, n) # a matrix with rows=samples, cols=features
    w_true = np.random.rand(n, 1) # col vector w with a weight for each feature
    b_true = np.random.rand(1) # random float bias

    y = np.dot(w_true.T, X) + b_true + np.random.normal(scale=0.1, size=(1, m))

    return X, y
