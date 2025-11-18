from random import randint
n = int(input("Podaj liczbę naturalną:\n".strip()))
a = [randint(-100, 100) for i in range(1, n+1)]
print(a)

a_parzyste = []
c = element % 10 for element in a
while True:
    for c in a:
        if c % 2 == 0:
            a_parzyste.append(c)
    print(a_parzyste)
