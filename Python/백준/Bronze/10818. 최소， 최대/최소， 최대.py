N = int(input())

N_list = list(map(int, input().split()))
N_list.sort()
print(N_list[0], N_list[N-1])