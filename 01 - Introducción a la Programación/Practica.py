#print('Hola Mundo!222')
# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
x=1
print(x)
# 2. Imprimir el tipo de dato de la constante 8.5
print(type(8.5))
# 3. Imprimir el tipo de dato de la variable creada en el punto 1
print(type(x))
# 4. Crear una variable que contenga tu nombre
nombre="Jhonatan Juan Carlos Delgado Gómez"
# 5. Crear una variable que contenga un número complejo
im = 5j
# 6. Mostrar el tipo de dato de la variable crada en el punto 5
print(type(im))
# 7. Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
import math
print(round(math.pi,4))
# 8. Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
b1 = True
b2 = True
print(b1==b2)
# 9. Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(b1))
# 10. Asignar a una variable, la suma de un número entero y otro decimal
suma = 1+1.5
# 11. Realizar una operación de suma de números complejos
i1 = 2+5j
scom = (4+5j) + i1
print(scom)
# 12. Realizar una operación de suma de un número real y otro complejo
sum = i1 + 5
print(sum)
# 13. Realizar una operación de multiplicación
mult = 5*5
# 14. Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
# 15. Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
a = 27/4
print(a)
# 16. De la división anterior solamente mostrar la parte entera
print(int(a))
# 17. De la división de 27 entre 4 mostrar solamente el resto
b = 27%4
print(a)
# 18. Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
a = 4*b+a
print(a)

j = "Jhonatan"
jj = " Juan Delgado"
print(j+jj)
print(int("2")==2)

# a = float('3j8')  ERROR POR LA COMA
a = float('3.8')

a = 3
a -= 3
print(a)

print(1<<3)