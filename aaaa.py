#tu na poczatku te #usr bin cos tam z geane skopiuj nastepnym razem chuj wie na co ale zrobisz raz to juz bedzie i wyjebane

def NWD(m,n):               #Zad 6 lista 3a

   while n != 0:
        m, n = n, m % n

   return m

def NWW(m,n):

    return (m * n) // NWD(m, n)

'''''
print("Podaj kolejno licznik i mianownik pierwszego ułamka, gdzie zarówno licznik jak i mianownik są nie większe od 100:\n")
a = int(input("Licznik a:"))
b = int(input("Mianownik b:"))
print()

print("Analogicznie proszę podać licznik i mianownik drugiego ułamka:\n")
c = int(input("Licznik c:"))
d = int(input("Mianownik d:"))

if a == 0 or b == 0 or c == 0 or d == 0:
    print("Mianownik nie może być zerem")
elif a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Wszystkie liczby muszą być większe od zera")
elif a > 100 or b > 100 or c > 100 or d > 100:
    print("Wszystkie liczby muszą być nie większe niż 100")
else:
    
    mianownik = NWW(b, d)
    licznik1 = a*mianownik//b
    licznik2 = c*mianownik//b
    
print(f"{int(licznik1)}/{int(mianownik)}, {int(licznik2)}/{int(mianownik)}")


#Zad 7
n = int(input("NWD ilu liczb naturalnych nie większych niż 100 mam obliczyć?\n"))      

wynik = int(input("Podaj liczbę:"))                  #wczytanie pierwszej liczby jako początkowy wynik

for _ in range(n - 1):                               #w pętli dla pozostałych n-1 liczb program wczytuje kolejną liczbę, oblicza NWD dotychczasowego wyniku z nową liczbą po czym aktualizuje zmienną wynik i zapamietuje. Genialne, czyż nie?
    wynik = NWD(wynik, int(input("Podaj liczbę:")    #program wykorzustuje te wskazowke wiec jest git

print(f"NWD wszystkich liczb wynosi: {wynik}")       #czyli jeszcze raz: zmienna wynik cały czas przechowuje NWD wszystkich dotychczas wczytanych liczb, więc przy każdym nowym wejściu obliczamy NWD tego dotychczasowego wyniku z nową liczbą, co daje nam NWD wszystkich liczb do tej pory i dzięki temu nie musimy pamiętać wszystkich liczb w tablicy. Jednym słowem: genialne


#Zad 8
w = [(0,7), (7,0), (7,-3), (-3,-3), (-3, 0)]      #wersja z indeksami
n = len(w)
k = 1
for i in range(n - 1):
    print(f"bok {k}:", end="  ")
    print(f"P1 = {w[i]}, P2 = {w[i + 1]}")
    k += 1
print(f"bok 5:  P1 = {w[-1]}, P2 = {w[0]}")

print()

P1 = w[0]                              #wersja bez indeksow
for P2 in w[1:]:
    print(f"P1 = {P1}, P2 = {P2}")
    P1 = P2                            #jak idziemy po elementach to trzeba pamietac o zamianie starego elementu na nowy tak jak tu
P2 = w[0]
print(f"P1 = {P1}, P2 = {P2}")

#dokończyc tak żeby liczylo ile punktów kratowych zawiera się w całym obwodzie tego wielokąta zgodnie z tym wzorem z NWD

x1, y1 = w[0][0], w[0][1]     #odwołanie do współrzędnych
x2, y2 = w[1][0], w[1][1]
x3, y3 = w[2][0], w[2][1]
x4, y4 = w[3][0], w[3][1]
x5, y5 = w[4][0], w[4][1]

dx1, dy1 = abs(x1 - x2), abs(y1 - y2)
dx2, dy2 = abs(x2 - x3), abs(y2 - y3)
dx3, dy3 = abs(x3 - x4), abs(y3 - y4)
dx4, dy4 = abs(x4 - x5), abs(y4 - y5)
dx5, dy5 = abs(x5 - x1), abs(y5 - y1)

punkty_bok1 = NWD(dx1, dy1)          #liczba p kratowych na bok ale juz bez dodawania 1 na koncu żeby nie liczyc po dwa razy tych samych wierzcholkow
punkty_bok2 = NWD(dx2, dy2)
punkty_bok3 = NWD(dx3, dy3)
punkty_bok4 = NWD(dx4, dy4)
punkty_bok5 = NWD(dx5, dy5)

punkty_suma = punkty_bok1 + punkty_bok2 + punkty_bok3 + punkty_bok4 + punkty_bok5
print()
print(f"W całym obwodzie tego wielokąta liczba punktów kratowych wynosi {punkty_suma}", end=" ")
'''

#Zad 9
from random import randint
def losowanie_bez_powtorzen():

    liczby = list(range(1, 50))
    print(liczby); print()
    wylosowane = []

    for i in range(6):
        losowy_indeks = randint(0, len(liczby) - 1)
        wylosowane.append(liczby.pop(losowy_indeks))  #wypluwamy z tamtej listy z ktorej losujemy wylosowana liczbe po jej indeksie dzieki czemu juz drugi raz tej samej liczby nie wylosujemy, wszystko to w jednej linijce :)
        print(f"Losowanie {i+1}: {wylosowane[-1]}")   #[-1] dlatego ze wczesniej wylosowane elementy zostaja w tej liscie wylosowane a my w kazdym z 6 losowan chcemy pokazac tylko ten z danego losowania czyli ostatni element, stąd ten indeks [-1]

    return wylosowane
print(losowanie_bez_powtorzen())
print()

#wersja wykorzystujaca te wskazowke (zamienianie wylosowanej liczby z ostatnia z listy itd)
def losowanie_zamiana():
    liczbyy = list(range(1, 50))
    wylosowane2 = []

    for i in range(6):
        losowy_indekss = randint(0, len(liczbyy) - 1 - i)
        wylosowana_liczba = liczbyy[(losowy_indekss)]
        wylosowane2.append(wylosowana_liczba)
        liczbyy[(losowy_indekss)], liczbyy[len(liczbyy) - 1 - i ] = liczbyy[len(liczbyy) - 1 - i], liczbyy[losowy_indekss]
        print(f"Losowanie {i + 1}: {wylosowane2[-1]}")

    return wylosowane2
print(losowanie_zamiana())









