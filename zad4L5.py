#!/usr/bin/env python3
'''
with open("dane.txt", "r") as dane, open("testuj.txt", "w") as t:  #z założeniem że nie ma spacji i pod ostatnia liczba jest enter
	t.writelines(set(dane.readlines()))
'''
with open("dane.txt", "r") as dane, open("testuj.txt", "w") as t:
	lista = []
	for d1 in dane:
		if int(d1) not in lista:
			lista.append(int(d1))
			t.write(str(int(d1)) + "\n")



    
    
    
    
    
    
    
    
    
    
    
    

