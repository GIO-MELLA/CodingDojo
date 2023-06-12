print( "----------------------------------------" )

# 1. 
print( "Hola, mundo\n" )

# 2a. 
name = "Giovanna"
print( "¡ Hola,", name ,"!" )	# con una coma

# 2b.
print( "Hola :) "+ name +"\n" )	# con un +

# 3a.
num = 30
print( "Hola, ", num )	# con una coma
# 3b.
print( "Hola número "+ str(num) )	# con una +	-- este debería arrojar un error!

#ninja
print( f"Hola, número {num} \n" )

# 4
fave_food1 = "Sushi"
fave_food2 = "Hamburguesas"

# a.
texto = "¡¡¡ Amo comer {} y {} !!! \n".format(fave_food1,fave_food2)
print("[ Con .format: ]")
print(texto)

# b.
print("[ Con cadena f: ]")
print( f"Amo comer {fave_food1} y {fave_food2}" )

print( "----------------------------------------\n" )

# Giovanna Mella