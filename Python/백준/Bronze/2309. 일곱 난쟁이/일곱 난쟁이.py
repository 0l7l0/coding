cm = [int(input()) for _ in range(9)]
sum1 = sum(cm)

for i in range(9):
    for j in range(i+1,9,1):
        if sum1 - (cm[i]+cm[j]) == 100:
            del cm[j]
            del cm[i]
            cm.sort()
            for h in cm:
                print(h)
            exit()