def even(a):
    if a % 2 == 0:
        return 1
    else:
        return 0


a = int(input())

if even(a):
    print("Even")
else:
    print("Not even")

