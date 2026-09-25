def sonlar(son):
    natija = []

    for x in son:
        if x < 0:
            natija += [x*-1]
        else:
             natija += [x]

    return natija
sn = [-3, 2, -1]
print(sonlar(sn))