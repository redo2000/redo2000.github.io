t = float(input ("Entrez la valeur de la durée en seconde:  "))
vs = 340 
g = 9.81
a = 1/vs 
b = (2/g)**0.5
c = -t 
delta = (b**2)-4*(a*c )
h= ((-b+delta**0.5)/(2*a))**2 
t1 = (2*h/g)**0.5
t2 = h/vs 
print()
print()
print()
print ("La profondeur est                  :",round(h,2),"m")
print()
print ("La durée de la chute est           :",round(t1,2),"s")
print()
print("La durée de propagation du son est :" ,round(t2,2),"s")
print()
print()
print()
print()