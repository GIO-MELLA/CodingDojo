# respuesta 1
print("------------1------------")

x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x, "\n")

print("original: ", estudiantes)
estudiantes[0]['last_name'] = 'Bryant'
print("actualizado: ", estudiantes, "\n")

print("original: ", directorio_deportes)
directorio_deportes['fútbol'][0] = 'Andrés'
print("actualizado: ", directorio_deportes, "\n")

z[0]['y'] = 30
print(z, "\n")


#respuesta 2
print("------------2------------")

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):

    for i in range (0, len(some_list)):
        infotxt = ""

        for key, val in some_list[i].items():
            infotxt += f" {key} - {val},"
        print(infotxt)

iterateDictionary(estudiantes)


#respuesta 3
print("------------3------------")

estudiantes = [
         {'name':  'Michael', 'last_name' : 'Jordan'},
         {'name' : 'John', 'last_name' : 'Rosales'},
         {'name' : 'Mark', 'last_name' : 'Guillen'},
         {'name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, some_list):
        for i in range (0, len(some_list)):
            print(some_list[i][key_name])

iterateDictionary2('name', estudiantes)
print("-------------------------")
iterateDictionary2('last_name', estudiantes)


#respuesta 4
print("------------4------------")

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo():

    print("------------------\n", len(dojo['ubicaciones']), "UBICACIONES : \n")

    for i in range(0, len(dojo['ubicaciones'])):
        print(dojo['ubicaciones'][i])
    
    print("------------------\n", len(dojo['instructores']), "INSTRUCTORES : \n")

    for i in range(0, len(dojo['instructores'])):
        print(dojo['instructores'][i])

printInfo()

# Giovanna Mella