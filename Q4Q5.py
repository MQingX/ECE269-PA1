import numpy as np

def buildTable(H):
    row_h, col_h =H.shape
    E = np.zeros((col_h,(col_h+1)))
    #`1-norm at most one --- For each row i, assume that E_ii==1
    for i in range(0,col_h):
        E[i,i]=1
    S=np.dot(H, E)
    return E,S

#test, using the matrix H which is mentioned before
H = np.array([[1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
              [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
              [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]])
E,S=buildTable(H)
print("Shape of H:", H.shape)
print("E:")
print(E)
print("Shape of E:", E.shape)
print("S:")
print(S)
print("Shape of S:", S.shape)