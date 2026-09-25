def raqamlar_soni(matn):
    sanoq = 0

    for belgi in matn:
        if '0' <= belgi <= '9':
            sanoq += 1

    return sanoq

print(raqamlar_soni("abc123"))
