def manfiylar(sonlar):
    natija = []

    for son in sonlar:
        if son < 0:
            natija += [son]

    return natija

print(manfiylar([3, -1, 0, -7]))



  