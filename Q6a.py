import numpy as np

def channelDecode(H,r):
    s_=np.dot(H,r)
    s=s_%2
    E,S=buildTable(H)
    col_s = S.shape[1]
    index = list(np.argwhere([(S[:,i]==s).all() for i in range(0,col_s)]))
    e = E[:,index[0][0]]
    x = np.abs(r-e)
    return e,x


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

#test, using the example x1 which is mentioned before as r
r = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
e,x=channelDecode(H,r)
print("When r^T = [1 1 1 1 1 0 0 0 0 1 0 0 0 0 0]")
print("e:")
print(e)
print("x:")
print(x)

