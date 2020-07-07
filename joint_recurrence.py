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

def recurrence_matrix(data, dimension, delay, threshold, norm):
    N = int(len(data) - (dimension-1) * delay)
    distance_matrix_1 = distance_matrix(data, dimension, delay, norm)
    for i in range(N):
        for j in range(i, N, 1):
            if distance_matrix_1[i,j] <= threshold:
                distance_matrix_1[i,j] = distance_matrix_1[j,i] = 1
            else:
                distance_matrix_1[i,j] = distance_matrix_1[j,i] = 0
    return distance_matrix_1.astype(int)

def joint_matrix(data1, data2, dimension1, dimension2, delay1, delay2, threshold1, threshold2, norm1, norm2):
    N1 = int(len(data1) - (dimension1-1) * delay1)
    N2 = int(len(data2) - (dimension2-1) * delay2)
    assert N1 == N2, "Space phase must have the same size"
    recurrence_matrix_1 = recurrence_matrix(data1, dimension1, delay1, threshold1, norm1)
    recurrence_matrix_2 = recurrence_matrix(data2, dimension2, delay2, threshold2, norm2)
    for i in range(N1):
        for j in range(i, N1, 1):
            if recurrence_matrix_1[i,j] == 1 and recurrence_matrix_2[i,j] == 1:
                recurrence_matrix_1[i,j] = recurrence_matrix_1[j,i] = 1
            else:
                recurrence_matrix_1[i,j] = recurrence_matrix_1[j,i] = 0
    return recurrence_matrix_1.astype(int)
