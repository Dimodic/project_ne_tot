import numpy as np

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2).tolist()

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2).tolist()

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2).tolist()

def determinant(matrix):
    return np.linalg.det(matrix)