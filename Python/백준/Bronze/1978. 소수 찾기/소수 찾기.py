from math import sqrt
N = int(input())
A = list(map(int,input().split()))
count = 0

for i in range(N):
    if A[i] == 2: 
        count += 1
        continue
    elif A[i] % 2 == 0 or A[i] == 1: 
        continue
    for j in range(3, int(sqrt(A[i]))+1, 2):
        if A[i] % j == 0:
            break
    else: 
        count += 1
print(count)