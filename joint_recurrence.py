import numpy as np

def distance_matrix(data, dimension, delay, norm):
    N = int(len(data) - (dimension-1) * delay)
    distance_matrix = np.zeros((N, N), dtype="float32")
    if norm == 'manhattan':     
        for i in range(N):
            for j in range(i, N, 1):
                temp = 0.0
                for k in range(dimension):
                    temp += np.abs(data[i+k*delay] - data[j+k*delay])
                distance_matrix[i,j] = distance_matrix[j,i] = temp
    elif norm == 'euclidean':
        for i in range(N):
            for j in range(i, N, 1):
                temp = 0.0
                for k in range(dimension):
                    temp += np.power(data[i+k*delay] - data[j+k*delay], 2)
                distance_matrix[i,j] = distance_matrix[j,i] = np.sqrt(temp)
    elif norm == 'supremum':
        temp = np.zeros(dimension)
        for i in range(N):
            for j in range(i, N, 1):
                for k in range(dimension):
                    temp[k] = np.abs(data[i+k*delay] - data[j+k*delay])
                distance_matrix[i,j] = distance_matrix[j,i] = np.max(temp)
    return distance_matrix

def joint_matrix(data1, data2, dimension, delay, threshold, norm):
    N1 = len(data_1)
    N2 = len(data_2)
    assert N1 == N2, "Time series must have the same size"
    distance_matrix_1 = distance_matrix(data1, dimension, delay, norm)
    distance_matrix_2 = distance_matrix(data2, dimension, delay, norm)
    N = len(distance_matrix_1[:,0])
    for i in range(N):
        for j in range(i, N, 1):
            if distance_matrix_1[i,j] <= threshold and distance_matrix_2[i,j] <= threshold:
                distance_matrix_1[i,j] = distance_matrix_1[j,i] = 1
            else:
                distance_matrix_1[i,j] = distance_matrix_1[j,i] = 0
    return distance_matrix_1.astype(int)
