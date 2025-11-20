#!/usr/bin/env python3
'''def nazwa(a):          #funkcje rekurencyjne lista 6A
	if a > 4:
		print("wywolanie funkcji przed return")
		return a
	print("wywolanie funkcji po return")
	return 10 * a
x = nazwa(1)
print("AAAA!!!!", x)


#Zad 1
def silnia(n):
	if n == 0:
		return 1
	return n * silnia(n-1)
print(silnia(0)), print(silnia(1)), print(silnia(2)), print(silnia(3)), print(silnia(4))
print()

#Zad 2
def newton(n, k):
	if k == 0 or k == n:
		return 1
	return newton(n-1, k-1) + newton (n-1, k)
print(newton(4,2))
print(newton(9,3))
'''

#Zad 3
'''
def nwd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def nwd_rek(a, b):
	if b == 0 and a != 0:
		return a
	if a == 0 and b != 0:
		return b
	return(nwd_rek(b, a % b))
print(nwd_rek(6,12), nwd_rek(0,4), nwd_rek(4,0))

#Zad 4
def mccarthy(n):
	if n > 100:
		return n -10
	return mccarthy(mccarthy(n + 11))
print(mccarthy(92), mccarthy(234))

#Zad 5
def ack(m, n):
	if m == 0:
		return n + 1
	if m > 0  and n == 0:
		return ack(m - 1, 1)
	return ack(m -1, ack(m, n -1))
print(ack(1, 0), ack(3, 2))

#Zad 6
def Fib(m):
	if m == 0:
		return 0
	if m == 1:
		return 1
	return Fib(m - 1) + Fib(m - 2)
print()

def Lucas(m):
	if m == 0:
		return 2
	if m == 1:
		return 1
	return Lucas(m - 1) + Lucas(m - 2)
print()

def slowa_fib1(m):
	if m == 0:
		return "b"
	if m == 1:
		return "a"
	return slowa_fib1(m - 1) + slowa_fib1(m - 2)
print()
	
def slowa_fib2(m):
	if m == 0:
		return "0"
	if m == 1:
		return "01"
	return slowa_fib2(m - 1) + slowa_fib2(m - 2)
'''
#Zad 6 ale wszystkie w jednym
def fib(m, a, b):
	if m == 0:
		return a
	if m == 1:
		return b
	return fib(m - 1, a, b) + fib(m - 2, a, b)
print(fib(5, 0, 1), fib(5, 2, 1), fib(5, "b", "a"), fib (5, "0", "01"))
	
	
	
