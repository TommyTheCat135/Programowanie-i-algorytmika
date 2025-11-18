def czy_ciekawocyfrowa(n):
    n = str(n)

    if len(n) == 1:
        return True

    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            return False

    return True

a = int(input("Podaj liczbę:\n"))
print(czy_ciekawocyfrowa(a))
