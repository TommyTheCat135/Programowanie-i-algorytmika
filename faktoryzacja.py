
def faktoryzacja(n):   #funkcja rozkładająca podaną przez użytkownika liczbę na czynniki zwracająca te czynniki w formie listy

    czynniki = []
    d = 2

    while d*d <= n:
        while n % d == 0:
            czynniki.append(d)
            n //= d
        d += 1

    if n > 1:   #jeśli po tym wszystkim z n wciaz jeszcze cos zostalo dodaj to do listy
        czynniki.append(n)

    return czynniki


def faktoryzacja_wyswietleniejakoiloczyn(n):  #funkcja której zadaniem jest ukazanie dokonań wczesniejszej funkcji użytkownikowi w przejrzystej formie iloczynu czynników

    czynniki = faktoryzacja(n)

    print(f"Rozkład na czynniki liczby {n} prezentuje się następująco:\n")

    iloczyn_czynnikow = " * ".join(str(a) for a in czynniki)
    print(f"{n} = {iloczyn_czynnikow}")


#mamy już opisane funkcje, pora więc na działanie ze strony użytkownika
n = int(input("Podaj liczbę naturalną większą od 1:\n".strip()))
print()

if not n > 1:
    pass

else:
    faktoryzacja_wyswietleniejakoiloczyn(n)
