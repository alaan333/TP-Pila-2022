# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
# uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from pila import Pila

raccoon={'nombre':'Rocket Raccoon','cant_peliculas': 4}
groot={'nombre':'Groot','cant_peliculas': 4}
viuda={'nombre':'Black Widow','cant_peliculas': 7}
iron={'nombre':'Iron Man','cant_peliculas': 9}
capitan={'nombre':'Capitan America','cant_peliculas': 11}
thor={'nombre':'Thor','cant_peliculas': 9}
doctor={'nombre':'Doctor Strange','cant_peliculas': 7}
capitana={'nombre':'Capitana Marvel','cant_peliculas': 3}
gamora={'nombre':'Gamora','cant_peliculas': 4}
drax={'nombre':'Drax el Destructor','cant_peliculas': 4}

#Como quedaria la pila:
# drax
# gamora
# capitana
# doctor
# thor
# capitan
# iron
# viuda
# groot
# raccoon

pila1=Pila()
pila2=Pila()
class Detalles():
    nombre,c_pel=None,None

personajes=[raccoon,groot,viuda,iron,capitan,thor,doctor,capitana,gamora,drax]

pos=0

for i in range(len(personajes)):
    dato=Detalles()
    dato.nombre=personajes[i]['nombre']
    dato.c_pel=personajes[i]['cant_peliculas']
    pila1.apilar(dato)

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
# uno la cima de la pila;
while(not pila1.pilaVacia()):
    dato=pila1.desapilar()
    pila2.apilar(dato)
    pos+=1
    if (dato.nombre=='Rocket Raccoon'):
        pos_rr=pos
    else:
        (dato.nombre=='Groot')
        pos_g=pos
print()
print(f'Rocket Raccon se encuentra en {pos_rr}° posicion de la pila')
print(f'Groot se encuentra en {pos_g}° posicion de la pila')
print()
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece;
print('Personajes que aparecieron en mas de cinco peliculas: ')
while(not pila2.pilaVacia()):
    dato=pila2.desapilar()
    pila1.apilar(dato)
    if (dato.c_pel>5):
        print('-',dato.nombre)
        print(f'  Apareció en {dato.c_pel} peliculas')
        print()
    if (dato.nombre=='Black Widow'):
        c_viu=dato.c_pel
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
print(f'Black Widow aparecio en {c_viu} peliculas')
print()
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
print('Personajes cuyos nombres empiezan con C, D o G: ')
while(not pila1.pilaVacia()):
    dato=pila1.desapilar()
    if (dato.nombre[0]== 'C' or dato.nombre[0]== 'D' or dato.nombre[0]== 'G'):
        print('-',dato.nombre)