import random
import string

paises = ['Italia', 'España', 'Alemania', 'Polonia', 'Brasil', 'Colombia', 'Bosnia', 'Turquia', 'Croacia', 'Argentina', 'Corea del sur', 'Suecia', 'Dinamarca', 'Ecuador', 'Suiza', 'Estados Unidos', 'Camerun', 'Belgica', 'Nigeria', 'Chile', 'Paraguay', 'Francia', 'Rusia', 'Peru', 'Uruguay', 'Inglaterra', 'Portugal', 'Ghana', 'Mexico', 'Hungria', 'Noruega', 'Holanda']

'''

print ('GRUPO A \r\n')
for i in range (0, 4):
    valor = random.choice(paises)
    print (valor)
    paises.remove(valor)                


print ('\r\n------------\r\n')

print ('GRUPO B \r\n')
for i in range (0, 4):
    valor = random.choice(paises)
    print (valor)
    paises.remove(valor)                    


print ('\r\n------------\r\n')

print ('GRUPO C \r\n')
for i in range (0, 4):
    valor = random.choice(paises)
    print (valor)
    paises.remove(valor)                


print ('\r\n------------\r\n')

print ('GRUPO D \r\n')
for i in range (0, 4):
    valor = random.choice(paises)
    print (valor)
    paises.remove(valor)                


print ('\r\n------------\r\n')

print ('GRUPO E \r\n')
for i in range (0, 4):
    valor = random.choice(paises)
    print (valor)
    paises.remove(valor)                


print ('\r\n------------\r\n')

print ('GRUPO F \r\n')
for i in range (0, 4):
    valor = random.choice(paises)
    print (valor)
    paises.remove(valor)                


print ('\r\n------------\r\n')

print ('GRUPO G \r\n')
for i in range (0, 4):
    valor = random.choice(paises)
    print (valor)
    paises.remove(valor)                


print ('\r\n------------\r\n')

print ('GRUPO H \r\n')
for i in range (0, 4):
    valor = random.choice(paises)
    print (valor)
    paises.remove(valor)                

'''

for j in range (8): # EJECUTA 8 VECES 
    print('GRUPO ', string.ascii_uppercase[j], '\r\n') 
    for i in range (4): # EJECUTA 4 VECES
        valor = random.choice(paises) # elige un pais random de la lista
        print (valor) # imprime el pais random
        paises.remove(valor) # elimina el pais de la lista
    print('\r\n ♥ ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♥ \r\n ') # cuando termina de elegir 4 paises, imprime la linea  

 #basicamente lo que hace string.ascii_uppercase[j], es que magicamente te muestra todo el abecedario en un string
    #entonces yo le dije, del string ese, dame la posicion j. y como j es el indice del for
    #por cada pasada, j se va incrementeando entonces me va dando cada letra
