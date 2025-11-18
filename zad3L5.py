#!/usr/bin/env python3   

# ========= L5, ZAD3 ===========
#liczby1, liczby2 = [], []   #dane1 i dane2 w tym samym folderze

#with open("dane1.txt", 'r', encoding="utf-8") as plik1 , open("dane2.txt", 'r', encoding="utf-8") as plik2:
	
	#for linia in plik1:
		#liczby1.append(int(linia))                         #wersja z listami(nieoptymalna dla duzych plikow, teorytycznie tez akceptowalna)
	#for linia in plik2:
		#liczby2.append(int(linia))
	
#liczby = []
#liczby.extend(liczby1)
#liczby.extend(liczby2)
#liczby.sort()

#with open("wynik.txt", 'w', encoding="utf-8") as w:
	
#	for i in range(0, len(liczby)):
#		element = liczby[i]
#		w.write(str(element) + " ")

with open("dane1.txt", 'r') as d1, open("dane2.txt", 'r') as d2, open("wynik.txt", 'w') as w:
    n1 = d1.readline()
    n2 = d2.readline()
    while n1 and n2:                             #wersja z labow, bardziej optymalna
        n1, n2 = int(n1), int(n2)
        if n1 <= n2:
            w.write(str(n1) + " ")
            n1 = d1.readline()
        else:
            w.write(str(n2) + " ")
            n2 = d2.readline()
    while n1:                              #te while n1 oznacza jakby while True czyli jezeli na jakiejs linii w pliku d1 zostala jakas liczba a nie pusta linia to wówczas
        n1 = int(n1)
        w.write(str(n1) + " ")
        n1 = d1.readline()
    while n2:
        n2 = int(n2)
        w.write(str(n2) + " ")
        n2 = d2.readline()

