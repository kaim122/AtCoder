N = int(input())
A = [input() for _ in range(N)]

FLAG = 1
for i in range(N):
    for j in range(N):
        if A[i][j] == 'W':
            if A[j][i] == 'W' or A[j][i] == 'D':
                FLAG = -1
        if A[i][j] == 'L':
            if A[j][i] == 'L' or A[j][i] == 'D':
                FLAG = -1
        if A[i][j] == 'D':
            if A[j][i] == 'W' or A[j][i] == 'L':
                FLAG = -1

if FLAG == 1:
    print("correct")
elif FLAG == -1:
    print("incorrect")