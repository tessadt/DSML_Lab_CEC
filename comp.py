import numpy as np

an_array = np.array([1, 3])
print("first array",an_array)
another_array = np.array([1, 2])
print("second array",another_array)
comparison = an_array == another_array
equal_arrays = comparison.all()
print("after comparison")
print(equal_arrays)

