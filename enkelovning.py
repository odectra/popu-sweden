# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:38:18 2020

@author: Oskar_Privatdator
"""

# EN ÖVNING! KUL VA!?
#Ange värden för x och y
x = 1
y = 2

#Summera x och y till z. 
z = x+y


# Skriv ut z med hjälp utav print()
print(z)

# Vad är x och y för datatyper? använd type() och skriv ut med print() 
print(type(x))
# Skriv text mellan ' ' för både x2 och y2
x2 = 'a'
y2 = 'b'


# Summera x2 och y2 till z2. SKriv ut z2 mha print()
z2 = (x2+y2)
print(z2)


# Vad är x2 och y2 för datatyper? Använd type() tillsammans med print()
#print(type())
print(type(x2))


# Lägg ihop z och z2 som z3. Använd str() för att göra båda datatyperna 
# till strings. 
z3=str(z)*3+z2
print(z3)


# Nedan är en dictionary med hur många chins vi klarar
chins = {'oskar':3, 'hanna':13, "tomten":1, "arnold":20}

namn="hanna"
namn2=input('ange vem du vill kolla upp: ')

# Skriv ut chins med hjälp utav print()
print(chins)
print(chins['oskar'])

antal_chins=chins[namn2]
print(namn2 +" klarar "+ str(antal_chins)+" stycken")



# Ta bort nedan # för att se exempel
#print('Oskar klarar ' + str(antal_chins) + ' st chins')
if antal_chins >10:
    print("Oj, vad starkt!")
else :
    print("Kämpa på!")

# Hur många chins klarar Hanna?
#print(namn2 +" klarar "+ str(antal_chins)+ " stycken chins")
