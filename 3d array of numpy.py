import numpy as np 
array=np.array([[['A','B','C'],['D','E','F']],
               [['G','H','I'],['J','K','L']]])
print(array.ndim)
print(array[0][0][0])
# first index selects horizontally , second selects 1 list from nested list , 3rd selects index from that list
