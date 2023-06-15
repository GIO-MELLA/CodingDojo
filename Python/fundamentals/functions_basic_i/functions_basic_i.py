#1 
def number_of_food_groups():
    return 5
print(number_of_food_groups()) # imprime 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) # error no existe la primera funcion


#3 
def number_of_books_on_hold():
    return 5 
    return 10
print(number_of_books_on_hold()) # imprime el primer return 5


#4  
def number_of_fingers():
    return 5 
    print(10)
print(number_of_fingers()) # imprime return 5


#5
def number_of_great_lakes():
    print(5) #imprime 5
x = number_of_great_lakes()
print(x) # nada


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3)) # imprime 3 y 5


#7 2+5
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) # son diferentes tipos int vs string


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)  # imprime 100
    if b < 10:
        return 5
    else:
        return 10 # retorna 10
    return 7   # no estoy segura que retorne este 7
print(number_of_oceans_or_fingers_or_continents())


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # imprime 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # imprime 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # imprime 7 + 14 que es 21


#10
def addition(b,c):
    return b+c # imprime 3 + 5 que es 8
    return 10
print(addition(3,5))


#11
b = 500
print(b) # imprime 500
def foobar():
    b = 300
    print(b) 
print(b) # imprime 500
foobar() # imprime 300 al cambiar el valor de la variable b
print(b) # imprime 500


#12
b = 500
print(b) #imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b) # imprime 500
foobar() # imprime 300 y no asigna el retorno de 300 a ninguna variable
print(b) # imprime 500


#13
b = 500
print(b) # imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b) # imprime 500
b=foobar() # imprime 300 y le asigna el valor de retorno a b (300)
print(b) # imprime 300


#14
def foo():
    print(1) 
    bar() 
    print(2) 
def bar():
    print(3)
foo() # imprime 1, llama a bar e imprime 3, imprime el 2


#15
def foo():
    print(1) # imprime 1
    x = bar() # llama a bar imprime el 3, le asigna el 5 a x
    print(x) # imprime el 5
    return 10  
def bar():
    print(3)
    return 5
y = foo() # foo() retorna el 10 y se lo asigna a y
print(y) # se imprime 10

# Giovanna Mella