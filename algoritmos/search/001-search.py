def busca_linear(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i + 1
    return None
