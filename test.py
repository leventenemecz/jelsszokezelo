import random

def velSzoveg(db)
	szoveg="ABCDEFGHIJKLMNPQRSTUVZ"
    j=""
	for x in range(0,3):
	j=j+szoveg[random.randint( 0,len(szoveg)-1 ): 
	return j
    szam="1234567890"
    j=""
	for x in range(0,2):
	j=j+szam[random.randint( 0,len(szoveg)-1 ): 
	return j
    kisbetu="abcdefghijklmnpqrstuvz"
    j=""
	for x in range(0,3):
	j=j+kisbetu[random.randint( 0,len(szoveg)-1 ): 
	return j
    j=""
	for x in range(0,5):
	j=j+szoveg[random.randint( 0,len(szoveg)-1 ): 
	return j
    jel="?"
    j=""
	for x in range(0,2):
	j=j+jel[random.randint( 0,len(szoveg)-1 ): 
	return j
    szam2="1234567890"
    j=""
	for x in range(0,1):
	j=j+szam2[random.randint( 0,len(szoveg)-1 ): 
	return j
    
	
	
print (velSzoveg(10))