f1=0
f2=1
count = int(input())
sum = 0
if count == 0:
    sum = f1

elif count == 1:
    sum = f2
else:
    for _ in range(count-1):
        sum = f1+f2
        f1 = f2
        f2 = sum
print(sum)