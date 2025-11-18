
# Wczytanie liczby
n = int(input("Podaj liczbę naturalną n: "))


# a) Podaj cyfrę jedności, dziesiątek, setek

cyfra_jednosci = n % 10
cyfra_dziesiatek = (n // 10) % 10 if n >= 10 else None
cyfra_setek = (n // 100) % 10 if n >= 100 else None

print("a) Cyfra jedności, dziesiątek, setek:")
print(f"   Cyfra jedności: {cyfra_jednosci}")
if cyfra_dziesiatek is not None:
    print(f"   Cyfra dziesiątek: {cyfra_dziesiatek}")
if cyfra_setek is not None:
    print(f"   Cyfra setek: {cyfra_setek}")
print()


# b) Wypisz cyfry od najmniej znaczącej

print("b) Cyfry od najmniej znaczącej:", end=" ")
temp = n
while temp > 0:
    print(temp % 10, end=" ")
    temp //= 10
print("\n")


# c) Oblicz sumę cyfr

suma = 0
temp = n
while temp > 0:
    suma += temp % 10
    temp //= 10
print(f"c) Suma cyfr liczby {n}: {suma}\n")


# d) Zapisz liczbę w systemie dwójkowym

if n == 0:
    binarny = "0"
else:
    binarny = ""
    temp = n
    while temp > 0:
        binarny = str(temp % 2) + binarny
        temp //= 2

print(f"d) Liczba {n} w systemie dwójkowym: {binarny}")
print(f"   (weryfikacja: {bin(n)})\n")


# e) Zapisz liczbę w systemie o podstawie p (2<=p<=10)

p = int(input("e) Podaj podstawę systemu (2-10): "))

if p < 2 or p > 10:
    print("   Podstawa musi być z przedziału [2, 10]\n")
else:
    if n == 0:
        wynik_p = "0"
    else:
        wynik_p = ""
        temp = n
        while temp > 0:
            wynik_p = str(temp % p) + wynik_p
            temp //= p

    print(f"   Liczba {n} w systemie o podstawie {p}: {wynik_p}\n")


# f) Oblicz liczbę cyfr w rozwinięciu binarnym

if n == 0:
    liczba_cyfr = 1
else:
    liczba_cyfr = 0
    temp = n
    while temp > 0:
        liczba_cyfr += 1
        temp //= 2

print(f"f)  Liczba cyfr w rozwinięciu binarnym liczby {n}: {liczba_cyfr}\n")

