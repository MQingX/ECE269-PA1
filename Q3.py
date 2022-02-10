import numpy as np

def checkCodeword(H, x):
    product=np.dot(H, x)
    if np.all(product%2==0):
        print("the vector x belongs to the codebook.")
    else:
        print("the vector x does not belong to the codebook.")

H = np.array([[1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
              [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
              [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]])
x1 = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0])
x2 = np.array([1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0])
x3 = np.array([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
x1_ = checkCodeword(H, x1)
x2_ = checkCodeword(H, x2)
x3_ = checkCodeword(H, x3)
print(x1_)
print(x2_)
print(x3_)