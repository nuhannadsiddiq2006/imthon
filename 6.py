def qiymatlar_yigindisi(lugat: dict) -> int:
    y = 0
    for i in  lugat:
        y += lugat[i]
    return y
print(qiymatlar_yigindisi({"a": 1, "b": 2, "c": 3}))
        
    