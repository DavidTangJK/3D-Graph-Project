import numpy as np

arr = []

for i in range(1, 61):
    arr_temp = [i] * 19
    arr = np.concatenate((arr, arr_temp))

y = arr
print(y)