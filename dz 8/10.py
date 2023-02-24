a = [int(i) for i in input().split()]
ma = max(a)
mi = min(a)
for i in range(len(a)):
    if a[i] == ma:
        a[i] = mi
    elif a[i] == mi:
        a[i] = ma

print(' '.join([str(i) for i in a]))
