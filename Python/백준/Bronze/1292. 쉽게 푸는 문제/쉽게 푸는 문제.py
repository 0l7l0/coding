a, b = map(int, input().split())
c = []

for i in range(1, b+1):
    for _ in range(1, i+1):
        c.append(i)
    
print(sum(c[a-1:b]))