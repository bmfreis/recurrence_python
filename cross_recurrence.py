import numpy as np

def distance_matrix(data1, data2, dimension, delay1, delay2, norm):
    N1 = int(len(data1) - (dimension-1) * delay1)
    N2 = int(len(data2) - (dimension-1) * delay2)
    distance_matrix = np.zeros((N1, N2), dtype="float32")
    if norm == 'manhattan':
        for i in range(N1):
            for j in range(N2):
                temp = 0.0
                for k in range(dimension):
                    temp += np.abs(data1[i+k*delay1] - data2[j+k*delay2])
                distance_matrix[i,j] = temp
    elif norm == 'euclidean':
        for i in range(N1):
            for j in range(N2):
                temp = 0.0
                for k in range(dimension):
                    temp += np.power(data1[i+k*delay1] - data2[j+k*delay2], 2)
                distance_matrix[i,j] = np.sqrt(temp)
    elif norm == 'supremum':
        temp = np.zeros(dimension)
        distance_matrix = np.zeros((N1, N2), dtype="float32")
        for i in range(N1):
            for j in range(N2):        
                for k in range(dimension):
                    temp[k] = np.abs(data1[i+k*delay1] - data2[j+k*delay2])
                distance_matrix[i,j] = np.max(temp)   
    return distance_matrix

def cross_matrix(data1, data2, dimension, delay1, delay2, threshold, norm):
    cross_matrix = distance_matrix(data1, data2, dimension, delay1, delay2, norm)
    N1 = len(cross_matrix[:,0])
    N2 = len(cross_matrix[0])
    for i in range(N1):
        for j in range(N2):
            if cross_matrix[i,j] <= threshold:
                cross_matrix[i,j] = 1
            else:
                cross_matrix[i,j] = 0
    return cross_matrix.astype(int)
