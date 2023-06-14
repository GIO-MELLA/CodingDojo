# Básico: imprime todos los números enteros del 0 al 150.
print("-------------Básico-------------")

for i in range(151):
    print(i)

print("---------------------------------\n")


# Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
print("-------Multiplos-de--Cinco-------")

for i in range(5, 1001):
    if i % 5 == 0:
        print(i)

print("---------------------------------\n")


# Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
print("----------Contar-Dojo------------")
for b in range(1, 101):
    
    if b % 10 == 0:
        print( b,"Coding Dojo" )

    elif b % 5 == 0:
        print( b, "Coding" )
    
    else:
        print(b)
print("---------------------------------\n")


# Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
print("---------Sumando-Impares---------")

sumando_impares = 0

for i in range(0, 500001):
    if i % 2 != 0:
        sumando_impares = sumando_impares + i

print( "Total: ", sumando_impares )
print("---------------------------------\n")


# Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

print("--------Cuenta-Regresiva---------")

num = 2018
for i in range(1, 2018):
    while num >= 0:
        print(num)
        num-=4

print("---------------------------------\n")


# Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

print("--------Contador-Flexible--------")

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print( i, "- ", end = "" )

print("\n---------------------------------\n")


# Giovanna Mella