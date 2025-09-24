n = 5
for i in range(1, n+1):
    print("*" * i)
for i in range(n):
    print("*" * (n-i-1))
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)