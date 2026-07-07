import random

def random_matrix(m,n, upper_bound=6, lower_bound=0):
    return [[random.randint(lower_bound, upper_bound) for _ in range(n)] for _ in range(m)]
    



matrix = random_matrix(5,5)
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



zero_striping(matrix)

print("*****"*20)

for r in matrix:
    print(r)