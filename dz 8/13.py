a = [int(s) for s in input().split()]
kol = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            kol += 1
print(kol)
