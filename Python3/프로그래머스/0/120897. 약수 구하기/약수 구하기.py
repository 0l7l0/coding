def solution(n):
    answer = []
    return sorted([ n//i for i in range(1,n+1) if n%i == 0])