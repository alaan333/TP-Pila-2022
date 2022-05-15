# Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
# desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
from pila import Pila

cont=0
pila1=Pila()
pila2=Pila()
class Peliculas():
    titulo, est_cine, a_estreno=None,None,None

interestelar={'titulo': 'Interestelar','anio_estreno':2014, 'est_cinem': 'Paramount'}
hobbit3={'titulo': 'El Hobbit 3','anio_estreno':2014, 'est_cinem': 'New Line Cinema'}
robocop={'titulo': 'RoboCop','anio_estreno':2014, 'est_cinem': 'Strike Entertainment'}
leg_diab={'titulo': 'El legado del diablo','anio_estreno':2018, 'est_cinem': 'PalmStar Media'}
rob_perf={'titulo': 'El robo perfecto','anio_estreno':2018, 'est_cinem': 'Diamond Film Productions'}
dr_strange={'titulo': 'Doctor Strange','anio_estreno':2016, 'est_cinem': 'Marvel Studios'}
cap_amer={'titulo': 'Capitan America: Civil War','anio_estreno':2016, 'est_cinem': 'Marvel Studios'}
iron_man={'titulo': 'Iron Man 3','anio_estreno':2013, 'est_cinem': 'Marvel Studios'}

titulos=[interestelar,hobbit3,robocop,leg_diab,rob_perf,dr_strange,cap_amer,iron_man]

for i in range(len(titulos)):
    dato=Peliculas()               #siempre poner ()
    dato.titulo=titulos[i]['titulo']
    dato.est_cine=titulos[i]['est_cinem']
    dato.a_estreno=titulos[i]['anio_estreno'] 
    #print(dato.titulo,' ',dato.est_cine,' ',dato.a_estreno)
    #print()
    pila1.apilar(dato)
    pila2.apilar(dato)

#--A--    
print('Peliculas estrenadas en el 2014: ')
while (not pila1.pilaVacia()):
    dato=pila1.desapilar()
    if(dato.a_estreno==2014):
        print('-',dato.titulo)
    #--B--
    if (dato.a_estreno==2018):
        cont+=1

#--B--
print()
print(f'Se estrenaron {cont} peliculas en el 2018')
print()

print('Películas de Marvel Studios estrenadas en el año 2016: ')
while (not pila2.pilaVacia()):
    dato=pila2.desapilar()
    if(dato.a_estreno==2016) and (dato.est_cine=='Marvel Studios'):
        print('-',dato.titulo)
print()  


    
         



