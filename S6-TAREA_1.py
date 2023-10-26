# Title: Tarea 1
# Estidiante: Juan Fernando Aviles Guillen
# Curso: C1-Nocturno

#1. Crea una lista de números enteros y calcula su suma.
print("----------------Ejercicio #1--------------------")
def ejer1():
    lista = [1,2,3,4,5]
    suma = 0
    for x in lista:
        suma += x
    print(f"La suma de los numeros de la lista es: {suma}")
ejer1()

print("\n----------------Ejercicio #2--------------------")

#2. Encuentra el número más grande en una lista de números
def ejer2():
    lista = [1,2,3,4,5]
    mayor = 0
    for x in lista:
        if x > mayor:
            mayor = x
    print(f"El numero mayor de la lista es: {mayor}")
ejer2()

print("\n----------------Ejercicio #3--------------------")

#3. Encuentra el número más pequeño en una lista de números.
def ejer3():
    lista = [5,12,43,24,15]
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    print(f"El numero menor de la lista es: {menor}")
ejer3()

print("\n----------------Ejercicio #4--------------------")
#4. Elimina los elementos duplicados de una lista.
def ejer4():
    lista = [1,2,3,4,5,1,2,3,4,5,6]
    lista2 = []
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    print(f"La lista sin elementos duplicados es: {lista2}")
ejer4()

print("\n----------------Ejercicio #5--------------------")
#5. Dada una lista, invierte su orden.
def ejer5():
    lista = [1,2,3,4,5]
    lista.reverse()
    print(f"La lista invertida es: {lista}")
ejer5()

print("\n----------------Ejercicio #6--------------------")
#6. Escribe un programa que cuente cuántas veces aparece un elemento en una lista.
def ejer6():
    lista = [1,2,3,4,5,1,2,3,4,5,6]
    numero = int(input("Ingrese un numero: "))
    print('el numero ingresado aparece', lista.count(numero), 'veces en la lista')
ejer6()

print("\n----------------Ejercicio #7--------------------")

#7. Crea una lista de números pares del 1 al 20.
def ejer7():
    lista = []
    for x in range(1,21):
        if x % 2 == 0:
            lista.append(x)
    print(f"La lista de numeros pares es: {lista}")
ejer7()

print("\n----------------Ejercicio #8--------------------")
#8. Dada una lista de nombres, ordénalos alfabéticamente.
def ejer8():
    lista = ["Juan","Christian","Evelyn","Lorena"]
    lista.sort()
    print(f"La lista de nombres ordenada alfabeticamente es: {lista}")
ejer8()

print("\n----------------Ejercicio #9--------------------")
#9. Crea una lista de los cuadrados de los números del 1 al 10.
def ejer9():
    lista = []
    for x in range(1,11):
        lista.append(x**2)
    print(f"La lista de los cuadrados de los numeros del 1 al 10 es: {lista}")
ejer9()

print("\n----------------Ejercicio #10--------------------")
#10. Dada una lista de números, encuentra el segundo número más grande.
def ejer10():
    lista = [1,2,3,4,5,6,16,8,1,20]
    lista.sort()
    print(f"El segundo numero mas grande de la lista es: {lista[-2]}")
ejer10()

print("\n----------------Ejercicio #11--------------------")
#11. Crea un diccionario con nombres de personas como claves y sus edades como valores.
def ejer11():
    diccionario = {"Juan":25,"Christian":30,"Evelyn":20,"Lorena":40}
    print(f"El diccionario es: {diccionario}")
ejer11()

print("\n----------------Ejercicio #12--------------------")
#12. Agrega un nuevo elemento a un diccionario.
def ejer12():
    diccionario = {"Juan":25,"Christian":30,"Evelyn":20,"Lorena":40}
    diccionario["Carlos"] = 35
    print(f"El diccionario es: {diccionario}")
ejer12()

print("\n----------------Ejercicio #13--------------------")
#13. Elimina un elemento de un diccionario por clave.
def ejer13():
    diccionario = {"Juan":25,"Christian":30,"Evelyn":20,"Lorena":40}
    del diccionario["Juan"]
    print(f"El diccionario es: {diccionario}")
ejer13()

print("\n----------------Ejercicio #14--------------------")
#14. Itera a través de las claves de un diccionario e imprime sus valores
def ejer14():
    diccionario = {"Juan":25,"Christian":30,"Evelyn":20,"Lorena":40}
    for x in diccionario:
        print(diccionario[x])
ejer14()

print("\n----------------Ejercicio #15--------------------")
#15. Verifica si una clave existe en un diccionario.
def ejer15():
    diccionario = {"Juan":25,"Christian":30,"Evelyn":20,"Lorena":40}
    clave = input("Ingrese una clave: ").capitalize()
    if clave in diccionario:
        print(f"La clave {clave} si existe en el diccionario")
    else:
        print(f"La clave {clave} no existe en el diccionario")
ejer15()

print("\n----------------Ejercicio #16--------------------")
#16. Dada una lista de diccionarios (personas), encuentra la persona más joven.
def ejer16():
    lista = [
        {"nombre":"Juan","edad":25},
        {"nombre":"Christian","edad":30},
        {"nombre":"Evelyn","edad":20},
        {"nombre":"Lorena","edad":40}
    ]
    lista.sort(key=lambda x:x["edad"])
    print(f"La persona mas joven es: {lista[0]}")
ejer16()

print("\n----------------Ejercicio #17--------------------")
#17. Dada una lista de diccionarios (libros), busca un libro por título.
def ejer17():
    lista = [
        {"titulo":"El Perfume","autor":"Patrick Süskind"},
        {"titulo":"Harry Potter","autor":"J.K Rowling"},
        {"titulo":"El principito","autor":"Antoine de Saint-Exupéry"},
        {"titulo":"Survival 1.12","autor":"ElRichMC"}
    ]
    titulo = input("Ingrese el titulo del libro: ").capitalize()
    for x in lista:
        if x["titulo"] == titulo:
            print(f"El libro {titulo} si existe en la lista")
            break
    else:
        print(f"El libro {titulo} no existe en la lista")
ejer17()

print("\n----------------Ejercicio #18--------------------")
#18. Crea un diccionario que cuente cuántas veces aparece cada palabra en una cadena de texto. sin contar las comas
def ejer18():
    cadena = "hola a todos, hola, que tal, mi nombre es Juan, y soy de Ecuador y esta es mi tarea de la semana 6"
    cadena = cadena.replace(",","")
    lista = cadena.split()
    diccionario = {}
    for x in lista:
        if x in diccionario:
            diccionario[x] += 1
        else:
            diccionario[x] = 1
    print(f"El diccionario es: {diccionario}")
ejer18()

print("\n----------------Ejercicio #19--------------------")
#19. Dado un diccionario de productos y sus precios, calcula el precio total de una lista de compras.
def ejer19():
    diccionario = {"tomate": 1, "pimiento": 2.5, "zanahoria":3, "arroz":2.5, "papa":5.5, "cebolla":3.3}
    lista = ["tomate","pimiento","cebolla"]
    suma = 0
    for x in lista:
        suma += diccionario[x]
    print(f"El precio total de la lista de compras es: {suma}")
ejer19()

print("\n----------------Ejercicio #20--------------------")
#20. Combina dos diccionarios en uno solo.
def ejer20():
    diccionario1 = {"tomate": 1, "pimiento": 2.5, "zanahoria":3, "arroz":2.5}
    diccionario2 = {"papa":5.5, "cebolla":3.3}
    diccionario1.update(diccionario2)
    print(f"El diccionario combinado es: {diccionario1}")
ejer20()

print("\n----------------Ejercicio #21--------------------")
#21. Usa un bucle while para contar del 1 al 10.
def ejer21():
    x = 1
    while x <= 10:
        print(x)
        x += 1
ejer21()

print("\n----------------Ejercicio #22--------------------")
#22. Usa un bucle for para imprimir los números pares del 1 al 20.
def ejer22():
    for x in range(1,21):
        if x % 2 == 0:
            print(x)
ejer22()

print("\n----------------Ejercicio #23--------------------")
#23. Escribe un programa que imprima los elementos de una lista utilizando un bucle for.

def ejer23():
    lista = [2,4,8,16,32]
    for x in lista:
        print(x)
ejer23()

print("\n----------------Ejercicio #24--------------------")
#24. Usa un bucle while para sumar los números del 1 al 100.
def ejer24():
    x = 1
    suma = 0
    while x <= 100:
        suma += x
        x += 1
    print(f"La suma de los numeros del 1 al 100 es: {suma}")
ejer24()

print("\n----------------Ejercicio #25--------------------")
#25. Escribe un programa que cuente cuántas veces aparece una letra en una cadena de texto utilizando un bucle for.
def ejer25():
    cadena = "hola a todos, hola, que tal, mi nombre es Juan, y soy de Ecuador y esta es mi tarea de la semana 6"
    letra = input("Ingrese una letra: ")
    contador = 0
    for x in cadena:
        if x == letra:
            contador += 1
    print(f"La letra {letra} aparece {contador} veces en la cadena")
ejer25()

print("\n----------------Ejercicio #26--------------------")
#26. Utiliza un bucle for para imprimir los números del 10 al 1 en orden decreciente.
def ejer26():
    for x in range(10,0,-1):
        print(x)
ejer26()

print("\n----------------Ejercicio #27--------------------")
#27. Escribe un programa que imprima los números impares del 1 al 30 usando un bucle for.
def ejer27():
    for x in range(1,31):
        if x % 2 != 0:
            print(x)
ejer27()

print("\n----------------Ejercicio #28--------------------")
#28. Usa un bucle while para encontrar el primer número divisible por 7 y 11.
def ejer28():
    x = 1
    while True:
        if x % 7 == 0 and x % 11 == 0:
            print(f"El primer numero divisible por 7 y 11 es: {x}")
            break
        x += 1
ejer28()

print("\n----------------Ejercicio #29--------------------")
#29. Escribe un programa que genere los primeros 10 números de la secuencia Fibonacci.
def ejer29():
    x = 0
    y = 1
    for z in range(10):
        print(x)
        x,y = y,x+y
ejer29()

print("\n----------------Ejercicio #30--------------------")
#30. Utiliza un bucle for para imprimir los elementos de una lista en reversa.
def ejer30():
    lista = [1,2,3,4,5,6,7,8,9,10]
    lista.reverse()
    for x in lista:
        print(x)
ejer30()

print("\n----------------Ejercicio #31--------------------")
#31. Escribe un programa que determine si un número es positivo, negativo o cero.
def ejer31():
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        print("El numero es positivo")
    elif numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")
ejer31()

print("\n----------------Ejercicio #32--------------------")
#32. Dado un número, verifica si es par o impar
def ejer32():
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
ejer32()

print("\n----------------Ejercicio #33--------------------")
#33. Escribe un programa que determine si un año es bisiesto.
def ejer33():
    año = int(input("Ingrese un año: "))
    if año % 4 == 0:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
ejer33()

print("\n----------------Ejercicio #34--------------------")
#34. Dada la edad de una persona, clasifícala como niño, adolescente, adulto o anciano.
def ejer34():
    edad = int(input("Ingrese su edad: "))
    if edad < 13:
        print("Usted es un niño")
    elif edad < 18:
        print("Usted es un adolescente")
    elif edad < 60:
        print("Usted es un adulto")
    else:
        print("Usted es un anciano")
ejer34()

print("\n----------------Ejercicio #35--------------------")
#35. Escribe un programa que determine si un triángulo es equilátero, isósceles o escaleno.
def ejer35():
    lado1 = int(input("Ingrese el lado 1: "))
    lado2 = int(input("Ingrese el lado 2: "))
    lado3 = int(input("Ingrese el lado 3: "))
    if lado1 == lado2 and lado1 == lado3:
        print("El triangulo es equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")
ejer35()

print("\n----------------Ejercicio #36--------------------")
#36. Dado un número, verifica si es primo o no.
def ejer36():
    numero = int(input("Ingrese un numero: "))
    contador = 0
    for x in range(1,numero+1):
        if numero % x == 0:
            contador += 1
    if contador == 2:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")
ejer36()

print("\n----------------Ejercicio #37--------------------")
#37. Escribe un programa que clasifique a un estudiante según su calificación (A, B, C, D, F).
def ejer37():
    nota = int(input("Ingrese su nota: "))
    if nota >= 90:
        print("Su nota es A")
    elif nota >= 80:
        print("Su nota es B")
    elif nota >= 70:
        print("Su nota es C")
    elif nota >= 60:
        print("Su nota es D")
    else:
        print("Su nota es F")
ejer37()

print("\n----------------Ejercicio #38--------------------")
#38. Dada una cadena de texto, verifica si es un palíndromo.
def ejer38():
    cadena = input("Ingrese una cadena de texto: ")
    cadena2 = cadena[::-1]
    if cadena == cadena2:
        print(f"La cadena {cadena} es un palindromo")
    else:
        print(f"La cadena {cadena} no es un palindromo")
ejer38()

print("\n----------------Ejercicio #39--------------------")
#39. Escribe un programa que determine si un número es divisible por 3 y 5.
def ejer39():
    numero = int(input("Ingrese un numero: "))
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"El numero {numero} es divisible por 3 y 5")
    else:
        print(f"El numero {numero} no es divisible por 3 y 5")
ejer39()

print("\n----------------Ejercicio #40--------------------")
#40. Dado un número, verifica si es positivo y múltiplo de 4.
def ejer40():
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        if numero % 4 == 0:
            print(f"El numero {numero} es positivo y multiplo de 4")
        else:
            print(f"El numero {numero} es positivo pero no es multiplo de 4")
    else:
        print(f"El numero {numero} no es positivo")
ejer40()

print("\n----------------Ejercicio #41--------------------")
#41. Crea una función que calcule el área de un triángulo. los valores deben estar defininidos en la funcion
def ejer41():
    def area_triangulo(base,altura):
        area = (base * altura) / 2
        return area
    print(f"El area del triangulo es: {area_triangulo(5,10)}")
ejer41()

print("\n----------------Ejercicio #42--------------------")
#42. Escribe una función que devuelva la longitud de una lista.
def ejer42():
    def longitud_lista(lista):
        return len(lista)
    lista = [5,12,23,44,53,100,89,"juan",]
    print(f"La longitud de la lista es: {longitud_lista(lista)}")
ejer42()

print("\n----------------Ejercicio #43--------------------")
#43. Crea una función que convierta grados Celsius a Fahrenheit.
def ejer43():
    def conversion(celsius):
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit
    print(f"La temperatura en grados Fahrenheit es: {conversion(100)}")
ejer43()

print("\n----------------Ejercicio #44--------------------")
#44. Escribe una función que genere una lista de números primos.
def ejer44():
    def numeros_primos(numero):
        lista = []
        for x in range(1,numero+1):
            contador = 0
            for y in range(1,x+1):
                if x % y == 0:
                    contador += 1
            if contador == 2:
                lista.append(x)
        return lista
    print(f"La lista de numeros primos es: {numeros_primos(50)}")
ejer44()

print("\n----------------Ejercicio #45--------------------")
#45. Crea una función que calcule el factorial de un número.
def ejer45():
    def factorial(numero):
        factorial = 1
        for x in range(1,numero+1):
            factorial *= x
        return factorial
    print(f"El factorial del numero es: {factorial(5)}")
ejer45()

print("\n----------------Ejercicio #46--------------------")
#46. Escribe una función que verifique si una cadena de texto es un pangrama (contiene todas las letras del alfabeto).
def ejer46():
    def pangrama(cadena):
        cadena = cadena.lower()
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for x in alfabeto:
            if x not in cadena:
                return False
        return True
    cadena = "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú."
    if pangrama(cadena):
        print(f"La cadena '{cadena}' es un pangrama")
    else:
        print(f"La cadena '{cadena}' no es un pangrama")
ejer46()

print("\n----------------Ejercicio #47--------------------")
#47. Crea una función que devuelva el número de vocales en una cadena de texto.
def ejer47():
    def vocales(cadena):
        contador = 0
        for x in cadena:
            if x in "aeiou":
                contador += 1
        return contador
    cadena = "hola a todos, hola, que tal, mi nombre es Juan, y soy de Ecuador y esta es mi tarea de la semana 6"
    print(f"El numero de vocales en la cadena es: {vocales(cadena)}")
ejer47()

print("\n----------------Ejercicio #48--------------------")
#48. Escribe una función que calcule el mínimo común múltiplo (MCM) de dos números.
def ejer48():
    def mcm(numero1,numero2):
        if numero1 > numero2:
            mayor = numero1
        else:
            mayor = numero2
        while True:
            if mayor % numero1 == 0 and mayor % numero2 == 0:
                break
            mayor += 1
        return mayor
    print(f"El minimo comun multiplo de los numeros es: {mcm(22,40)}")
ejer48()

print("\n----------------Ejercicio #49--------------------")
#49. Crea una función que verifique si una cadena de texto es un palíndromo.
def ejer49():
    def palindromo(cadena):
        cadena = cadena.replace(" ","")
        cadena2 = cadena[::-1]
        if cadena == cadena2:
            return True
        else:
            return False
    cadena = "anita lava la tina"
    if palindromo(cadena):
        print(f"La cadena '{cadena}' es una frase palindromo")
    else:
        print(f"La cadena '{cadena}' no es una frase palindromo")
ejer49()

print("\n----------------Ejercicio #50--------------------")
#50. Escribe una función que determine si un número es par o impar, que lo escriba el usuario el numero
def ejer50():
    def par_impar(numero):
        if numero % 2 == 0:
            return True
        else:
            return False
    numero = int(input("Ingrese un numero: "))
    if par_impar(numero):
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
ejer50()

print("\n----------------Ejercicio #51-52-53--------------------")
#51. Crea una clase llamada "Persona" con atributos nombre y edad.
#52. Crea un objeto de la clase "Persona" e imprime sus atributos.
#53. Agrega un método a la clase "Persona" para saludar.
def ejer51_52_53():
    class Persona:
        def __init__(self,nombre,edad):
            self.nombre = nombre
            self.edad = edad
        def saludar(self):
            print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
    persona = Persona("Juan",19)
    print(f"Nombre: {persona.nombre}")
    print(f"Edad: {persona.edad}")
    persona.saludar()
ejer51_52_53()

print("\n----------------Ejercicio #54-55--------------------")
#54. Crea una clase llamada "Rectángulo" con atributos largo y ancho.
#55. Agrega un método a la clase "Rectángulo" para calcular el área.
def ejer54_55():
    class Rectangulo:
        def __init__(self,largo,ancho):
            self.largo = largo
            self.ancho = ancho
        def area(self):
            area = self.largo * self.ancho
            return area
    rectangulo = Rectangulo(10,25)
    print(f"El area del rectangulo es: {rectangulo.area()}")
ejer54_55()

print("\n----------------Ejercicio #56-57--------------------")
#56. Crea una clase llamada "CuentaBancaria" con atributos saldo y titular.
#57. Agrega métodos para depositar y retirar dinero de la cuenta bancaria. y al final presentar el saldo
def ejer56_57():
    class CuentaBancaria:
        def __init__(self,saldo,titular):
            self.saldo = saldo
            self.titular = titular
        def depositar(self,cantidad):
            self.saldo += cantidad
        def retirar(self,cantidad):
            self.saldo -= cantidad if self.saldo >= cantidad else print("No hay suficiente saldo")
        def presentar(self):
            print(f"Titular: {self.titular}")
            print(f"Saldo: {self.saldo}")
    cuenta = CuentaBancaria(100,"Juan")
    cuenta.depositar(50)
    cuenta.retirar(25)
    cuenta.presentar()
ejer56_57()

print("\n--------------Ejercicio #58-59-60-------------------")
#58. Crea una clase llamada "Coche" con atributos marca, modelo y año.
#59. Agrega un método para acelerar el coche.
#60. Escribe un programa que cree una lista de objetos "Coche" y acelere cada uno de ellos.
def ejer58_59_60():
    class Coche:
        def __init__(self, marca, modelo, año):
            self.marca = marca
            self.modelo = modelo
            self.año = año
        def acelerar(self,velocidad):
            self.velocidad = velocidad
            return f'El coche {self.marca} - {self.modelo} está acelerando. Ahora va a {self.velocidad} km/h.'
    coche1 = Coche("Land Rover","Range Rover",2020,)
    coche2 = Coche("Hyundai","Accent",2018)
    coche3 = Coche("Lamborghini","Aventador",2019)
    acelerar1 = coche1.acelerar(10)
    acelerar2 = coche2.acelerar(25)
    acelerar3 = coche3.acelerar(300)
    print(f"Marca: {coche1.marca}, Modelo: {coche1.modelo}, Año: {coche1.año}")
    print(acelerar1)
    print(f"Marca: {coche2.marca}, Modelo: {coche2.modelo}, Año: {coche2.año}")
    print(acelerar2)
    print(f"Marca: {coche3.marca}, Modelo: {coche3.modelo}, Año: {coche3.año}")
    print(acelerar3)
ejer58_59_60()

print("\n-------------------------------------------------------------")

print("\nTarea por: Juan Fernando Aviles Guillen")

print("\n----------------------Fin de la Tarea------------------------")