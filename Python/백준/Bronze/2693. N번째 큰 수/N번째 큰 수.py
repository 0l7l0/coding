T = int(input())
N = 3
A = []
for i in range(T):
    A.append(list(map(int, input().split())))
    A[i].sort(reverse=True)
    
for j in range(T):
    print(A[j][2])