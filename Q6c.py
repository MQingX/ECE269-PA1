import numpy as np

def PossibleSignals2bits(x):
    n = x.shape[0]
    error = []
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            error_row=np.zeros(n)
            error_row[i]=1
            error_row[j]=1
            c=c+1
            error.append(error_row)
    error=np.array(error)
    signals = np.zeros((c,n))
    for k in range(0,c):
        x_ = np.transpose(x)
        signals[k,:] = (error[k,:] + x_)%2
    return signals

def Correct2bit(x):
    signals2 = PossibleSignals2bits(x)
    print("All possible received signals corresponding to the given x:")
    print(signals2)
    n = signals2.shape[0]
    c = 0
    for i in range(0, n):
        e_, x_ = channelDecode(H,signals2[i,:])
        if (x_ == x).all():
            c = c+1
    return c

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

#(1)
#transmit the given vector x
x6 = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
Correct_2bit=Correct2bit(x6)
print("When introducing error in 2 bits, we can successfully decode the transmitted signal", Correct_2bit, "times.")

#(2)
#repeat it several times for different x
x6_test1 = np.array([1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0])
Correct_2bit_test1=Correct2bit(x6_test1)
print("For x_test1 = np.transpose([1 0 0 1 1 0 0 1 0 1 0 0 0 0 0])")
print("When introducing error in 2 bits, we can successfully decode the transmitted signal", Correct_2bit_test1, "times.")

x6_test2 = np.array([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
Correct_2bit_test2=Correct2bit(x6_test2)
print("For x_test2 = np.transpose([1 0 0 0 1 0 0 0 0 0 0 0 0 0 1])")
print("When introducing error in 2 bits, we can successfully decode the transmitted signal", Correct_2bit_test2, "times.")