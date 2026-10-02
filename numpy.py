import numpy as np 
array=np.array([1,2,3])
array=array*2
print(array)
#the array instead of becomig 1 2 3 1 2 3 bewcomes 2, 4 ,6
#dimentsiona of arrays can be found out using array.ndim -- ndim stands for n dimensional
print(array.ndim)
array1=np.array([1,2,3],[1,2,3],
                [2,3,4],[3,4,5])
print(array1.ndim)

