T = int(input())
   
for _ in range(T):
    line = int(input())
    pos = 0
    while line> 0:
        if line & 1:
            print(pos, end = ' ')
        line >>=1
        pos += 1
    print()