big, small = map(int, input().split())
A = 0
temp = 0
mult = big * small
while True:
    if big % small == 0:
        A = small
        break
    else:
        temp = small
        small = big % small
        big = temp

B = mult // A 
print(A)
print(B)