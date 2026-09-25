def ikkilantir(sonlar):
    natija = []

    for son in sonlar:
        natija += [son * 2]

    return natija

print(ikkilantir([1, 2, 3]))