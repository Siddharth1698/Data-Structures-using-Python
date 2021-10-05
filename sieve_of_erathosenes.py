# Sieve of Erathosenes
def sieve(num):
    l = []
    for i in range(2, num + 1):
        l.append(i)

    for i in l:
        for j in range(2, num // 2):
            if i * j in l:
                l.remove(i * j)
    print(l)


sieve(50)
