#Programme qui permette de déterminer quelle somme aura Amal lors de son nième anniversaire. 
a=int(input("Entrer l'age de amal : "))
s=0
for i in range(1,a+1):
    s=s+(500+i*3)
print(f"La somme de l'argent de amal cette année est {s} Dh")