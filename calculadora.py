print('Bienvenido a mi primera calculadora, ¿Que operacion desea realizar?/n')

print('''
1. Sumar.
2. Restar.
3. Multiplicar.
4. Divivdir.
5. Comparar numeros.
6. Elevar un numero a otro
7. Valor Absoluto
''')
valor1=0
valor2=0
election=int(input("Escoge una opcion: "))


if election==1:
    valor1=int(input("Escoge el primer sumando: "))
    valor2=int(input("Escoge el segundo sumando: "))
    valor_total=valor2+valor1
    print(f"Suma: {valor_total} ")

elif election==2:
     valor1=int(input("Escoge el minuendo: "))
     valor2=int(input("Escoge el sustraendo: "))
     valor_total=valor1-valor2
     print(f"La diferencia es: {valor_total} ")
     
elif election==3:
     valor1=int(input("Escoge el multiplicador: "))
     valor2=int(input("Escoge el multiplicador: "))
     valor_total=valor1*valor2
     print(f"El producto es: {valor_total} ")
     
elif election==4:
     valor1=int(input("Escoge el Dividendo: "))
     valor2=int(input("Escoge el Divisor: "))
     if valor2==0:
         print("Error: valor indefinido ")
     else:
         valor_total=valor1/valor2
         print(f"El cociente es: {valor_total} ")
     
elif election==5:
     valor1=int(input("Escoge el valor1: "))
     valor2=int(input("Escoge el valor2: "))
     if valor1>valor2:
         print(f" {valor1} es mayor que {valor2} ")
     else:
         print(f" {valor2} es mayor que {valor1} ")


elif election==6:
     valor1=int(input("Escoge la base: "))
     valor2=int(input("Escoge el exponente: "))
     valor_total=valor1**valor2
     print(f"El resultado es : {valor_total} ")
     
elif election==7:
     valor1=int(input("Saca el valor absoluto"))
     if valor1>0:
         print(f" Es valor absoluto es: {valor1} ")
     else:
         valor1*=-1
         print(f"El valor absoluto es {valor1} ")
   
    
     
    
    