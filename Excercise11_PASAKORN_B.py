n = int(input("Please input number: "))
for z in range(n):
    print(" " * (n - z) + "*" * (2 * z + 1))