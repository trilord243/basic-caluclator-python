x=int(input("Verifique si su numero es oblongo "))
condicion=False
for i in range(x):
    if i*(i+1)==x:
        condicion=True
        break

if condicion:
        print("Es un numero oblongo ")
else:
    print("No es un numero oblongo ")



