import numpy as np
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries")

for i in range(row):		
	a =[]
	for j in range(col):	 
		a.append(int(input()))
	matrix.append(a)
print(matrix)
result =  np.transpose(matrix)
print("transpose of the matrix:")
print(result) 


