print("--------- 1 ---------")

lista_num = []

def countdown(i):
    while i >= 0:
        lista_num.append(i)
        i -= 1
    return lista_num
print(countdown(5))


print("\n--------- 2 ---------")

def imprimir_y_devolver(a,b):
    print(a)
    return b 
print(imprimir_y_devolver(1,2))


print("\n--------- 3 ---------")

lista_pml = []

def primero_mas_longitud(lista_pml):
    suma = lista_pml[0]+ len(lista_pml)
    return suma
print(primero_mas_longitud([1,2,3,4,5]))


print("\n--------- 4 ---------")

lista_original = []
lista_nueva = []

def valores_mayores_que_el_segundo(lista_original):
    lista_nueva.clear()
    if(len(lista_original)> 2):
        print("Largo lista original: ", len(lista_original))
        print("Lista original: ", lista_original)

        for i in range(0, len(lista_original)):

            if (lista_original[i] > lista_original[1]):
                lista_nueva.append(lista_original[i])
        
        print("Largo lista nueva: ", len(lista_nueva))
        return lista_nueva
            
    else:
        return False

print("Nueva lista: ", valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print("------------------------------------------")
print("Otra lista (ej -2 elementos): ", valores_mayores_que_el_segundo([3]))
print("------------------------------------------")


print("\n--------- 5 ---------")

lista_lav = []

def length_and_value(a,b):
    lista_lav.clear()
    while a > 0:
        lista_lav.append(b)
        a -= 1
    return lista_lav

print(length_and_value(4,7))
print(length_and_value(6,2))

# Giovanna Mella