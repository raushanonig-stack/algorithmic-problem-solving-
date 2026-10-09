def matrix_vector_multiply(matrix, vector):
    """
    Computes linear transformation (matrix-vector dot product)
    for computational modeling and data transforms.
    """
    if len(matrix[0]) != len(vector):
        raise ValueError("Matrix column count must match vector length.")
        
    result = []
    for row in matrix:
        dot_product = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(dot_product)
    return result

if __name__ == "__main__":
    A = [
        [1.5, 2.0, 0.0],
        [0.0, 3.2, 1.1],
        [4.0, 0.5, 2.3]
    ]
    x = [2.0, 1.0, 3.0]
    
    output = matrix_vector_multiply(A, x)
    print("Transformation Output:", output)
