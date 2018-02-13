#Taller 1 parte 2
print ("Datos: ")
ListaNumeros=[1,4,6,7,2,3,4,7,1,2,4,3,4,5,
      6,5,2,3,1,2,5,8,7,3,4,1,5,7,
      11,15,3,4,2,6,7,4,8,9,2,4,6,4,3,2,4,5,6,7,5,5,5,8,9,7,7,7,7,7,4,3,2,3,4]
print (ListaNumeros)
OrdenarNumeros=sorted(ListaNumeros)
Numeros=len(OrdenarNumeros)
middle = Numeros/2
print ("los numeros ordenaso son: ")
print(OrdenarNumeros)
print("El total de numeros son ",(Numeros))

#calcular la moda
repetir = 0
for i in ListaNumeros:
    aparece = ListaNumeros.count(i)
    if aparece > repetir:
        repetir = aparece
moda = []
for i in ListaNumeros:
    aparece =ListaNumeros.count(i)
    if aparece == repetir and i not in moda:
        moda.append(i)
print ("la moda es ",(moda))

#Promedio
print ("programa para saber el promedio de una lista de numeros")
lista=[2,3,4,7,6,5,4,5]

print ("La lista es ",(lista))
suma =0
i=0
for elemento in lista:
   suma =suma + elemento
   i=i+1
promedio = suma // i
print ("El promedio de los numeros es:  ",(promedio))
print ("La cantidad de numeros en la lista es de:  ",(i))
