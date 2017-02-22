#!/usr/bin/env python
cad1=input("Cadena:")	
if cad1.lower()==cad1[::-1].lower():
    print("palindromo")
else:
    print("no palindromo")
