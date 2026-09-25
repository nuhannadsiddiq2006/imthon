def faktorial(n):
    natija = 1
    i = 1

    while i <= n:
        natija *= i
        i += 1

    return natija

print(faktorial(5))