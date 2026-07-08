import random
from copy import deepcopy

def random_matrix(m,n, upper_bound=6, lower_bound=0):
    return [[random.randint(lower_bound, upper_bound) for _ in range(n)] for _ in range(m)]
    



matrix = random_matrix(5,5)
new_matrix = deepcopy(matrix)
for r in matrix:
    print(r)

def zero_striping(mat:list[list[int]])-> list[list[int]]:
    row = len(mat)
    column = len(mat[0])
    zero_row = set()
    zero_col = set()

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)
    
    for i in range(row):
        for j in range(column):
            if i in zero_row or j in zero_col:
                matrix[i][j] = 0  
            
    return matrix

# Time complexity is O(M*N) where M and N is size of the matrix
# Space complexity is O(M+N)

# Optimal solution will need to have lower space complexity.

def zero_striping_optimal(mat: list[list[int]]) -> list[list[int]]:
    row = len(mat)
    col = len(mat[0])

    first_row_contain_zero = False
    for i in range(row):
        if mat[i][0] == 0:
            first_row_contain_zero = True
            break
    
    first_column_contain_zero = False
    for j in range(col):
        if mat[0][j] == 0:
            first_column_contain_zero = True
            break

    for i in range(1, row):
        for j in range(1, col):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
    
    for i in range(1, row):
        for j in range(1, col):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
    
    if first_column_contain_zero:
        for i in range(col):
            mat[0][i] = 0
    
    if first_row_contain_zero:
        for i in range(row):
            mat[i][0] = 0

    return mat



zero_striping(matrix)

print("*****"*20)

for r in matrix:
    print(r)
print("*****"*20)
for r in new_matrix:
    print(r)

zero_striping_optimal(new_matrix)

print("*****"*20)

for r in new_matrix:
    print(r)