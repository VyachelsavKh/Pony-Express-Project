def dupl(a):
    a.sort()
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            return 1
    return 0

print(dupl([1,2,3,4,5]))
