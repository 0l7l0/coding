now_count = 0
most_count = 0

for _ in range(10):
    i , j = map(int, input().split())
    now_count -= i
    now_count += j
    
    if now_count > most_count:
        most_count = now_count
print(most_count)