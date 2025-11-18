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
n = int(input("NWD ilu liczb naturalnych nie większych 100 mam obliczyć?\n"))      #wczytanie n (liczby liczb XD)

wynik = int(input("Podaj liczbę:"))                #wczytanie pierwszej liczby jako początkowy wynik

for _ in range(n - 1):                             #w pętli dla pozostałych n-1 liczb program wczytuje kolejną liczbę, oblicza NWD dotychczasowego wyniku z nową liczbą po czym aktualizuje zmienną wynik i zapamietuje. Genialne, czyż nie?
    wynik = NWD(wynik, int(input("Podaj liczbę:")  #program wykorzustuje te wskazowke wiec jest git

print(f"NWD wszystkich liczb wynosi: {wynik}")     #czyli jeszcze raz: nasza zmienna wynik cały czas przechowuje NWD wszystkich dotychczas wczytanych liczb, więc przy każdym nowym wejściu obliczamy NWD tego dotychczasowego wyniku z nową liczbą, co daje nam NWD wszystkich liczb do tej pory i dzięki temu nie musimy pamiętać wszystkich liczb w tablicy. Jednym słowem: genialne
'''''

#Zad 8
w = [(0,7), (7,0), (7,-3), (-3,-3), (-3, 0)]      #wersja z indeksami
n = len(w)
for i in range(n - 1):
    print(f"P1 = {w[i]}, P2 = {w[i + 1]}")
print(f"P1 = {w[-1]}, P2 = {w[0]}")

print()

P1 = w[0]                              #wersja bez indeksow
for P2 in w[1:]:
    print(f"P1 = {P1}, P2 = {P2}")
    P1 = P2                            #jak idziemy po elementach to trzeba pamietac o zamianie starego elementu na nowy tak jak tu
P2 = w[0]
print(f"P1 = {P1}, P2 = {P2}")

#dokończyc tak żeby liczylo ile punktów kratowych zawiera się w całym obwodzie tego wielokąta zgodnie z tym wzorem ktory masz na zdjeciu


