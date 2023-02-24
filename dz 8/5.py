a = [int(i) for i in input().split()]
kol = 0
for i in range(1, len(a)-1):
    if a[i - 1] <a[i]  and a[i] > a[i+1]:
        kol += 1
print(kol)
a = [int(i) for i in input().split()]
kol = 0
for i in range(1, len(a)-1):
    if a[i - 1] <a[i]  and a[i] > a[i+1]:
        kol += 1
print(kol)
