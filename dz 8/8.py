a = [int(i) for i in input().split()]
kol = 1
for i in range(1,len(a)):
    if a[i - 1] !=a[i]:
        kol += 1
print(kol)
