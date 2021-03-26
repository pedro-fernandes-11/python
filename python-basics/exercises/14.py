n = int(input("N:"))

if n % 2 == 0:
    for i in range(n, -1, -1):
        if i % 2 == 0:
            print(i)
