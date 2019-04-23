def prastevila(n)   
    import math
    seznam == []
    while n < 200:
        i = 1
        while i < math.sqrt(n):
            if n % i == 0:
                seznam.append(n)
            i += 1
        n += 1
    return seznam


