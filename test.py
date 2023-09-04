import numpy as np

array = np.array([[[1,2,3],
                   [4,5,6],
                   [7,8,9]],
                  [[1,2,3],
                   [4,5,6],
                   [7,8,9]],
                  [[1,2,3],
                   [4,5,6],
                   [7,8,9]]],)
print(array)

array = np.rot90(array,1,(0,1))

print(array)