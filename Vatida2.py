#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

print("1)")
num = 41
print(num)
print(" ")

#2) Imprimir el tipo de dato de la constante 8.5

print("2)")
print(type(8.5))
print(" ")

#3) Imprimir el tipo de dato de la variable creada en el punto 1

print("3)")
print(type(num))
print(" ")

#4) Crear una variable que contenga tu nombre

print("4)")
name = "Agus"
print(name)
print(" ")

#5) Crear una variable que contenga un número complejo

print("5)")
com = 3j
print(com)
print(" ")

#6) Mostrar el tipo de dato de la variable crada en el punto 5

print("6)")
print(type(com))
print(" ")

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

print("7)")
pi = 3.1415
print(pi)
print(" ")

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

print("8)")
t1 = "True"
t2 = True
print(t1)
print(t2)
print(" ")

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print("9)")
print("Las clases son: ", type(t1), " y ", type(t2))
print(" ")

#10) Asignar a una variable, la suma de un número entero y otro decimal

print("10)")
suma = 5 + 0.4
print(suma)
print(" ")

#11) Realizar una operación de suma de números complejos

print("11)")
co = 3j - 12j
print(co)
print(" ")

#12) Realizar una operación de suma de un número real y otro complejo

print("12)")
suco = 5 + 3j
print(suco)
print(" ")

#13) Realizar una operación de multiplicación

print("13)")
mul = 7 * 8
print(mul)
print(" ")

#14) Mostrar el resultado de elevar 2 a la octava potencia

print("14)")
print(2**8)
print(" ")

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

print("15)")
dev = 27 / 4
print(dev)
print(" ")

#16) De la división anterior solamente mostrar la parte entera

print("16)")
dev2 = 27 // 4
print(dev2)
print(" ")

#17) De la división de 27 entre 4 mostrar solamente el resto

print("17)")
dev3 = 27 % 4
print(dev3)
print(" ")

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

print("18)")
print(4*6+3)
print(" ")


#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

print("19)")
print("Hola " + "Mundo")
print(" ")

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print("20)")
a = 2
b = "2"
print(a == b)
print(" ")

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print("21)")
print(a == int(b))
print(" ")

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

print("22)")
c = float("3.8")
print(c)
print(" ")

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

print("23)")
d = 3
d -= 3
print(d)
print(" ")

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

print("24)")
print(1 << 2)
print(" ")

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

print("25)")
print(2 + int("2"))
print(str(2) + "2")
print(float(2) + float("2"))
print(" ")

#26) Realizar una operación válida entre valores de tipo entero y string

print("26)")
print(str(2) + " horas")
