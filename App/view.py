"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import datetime



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar eventos de escucha en rango de instrumentalidad ")
    print("3- Buscar musica para festejar ")
    print("4- Buscar musica para estudiar ")
    print("5- Estudiar generos musicales ")
    print("6- Buscar genero mas escuchado entre dos horas ")

def printGenres():
    print("1. Reggae")
    print("2. Down-Tempo")
    print("3. Chill-out")

    print("4. Hip-hop")
    print("5. Jazz and Funk")
    print("6. Pop")

    print("7. R&B")
    print("8. Rock")
    print("9. Metal")

    print("10. Otro genero")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadEvents(catalog)
        print('Eventos cargados: ' + str(controller.repSize(catalog)))
        print('Altura del arbol: ' + str(controller.indexHeight(catalog)))

    elif int(inputs[0]) == 2:
        minChar = input("Ingrese el valor minimo: ")
        maxChar = input("Ingrese el valor maximo: ")
        char = input("Ingrese la caracteristica: ")
        total = controller.getCharacteristicByRange(catalog, minChar, maxChar, char)
        artists = controller.getArtists(catalog,minChar, maxChar, char)
        print("\nTotal de eventos de escucha en el rango de " + char + ": " + str(total))
        print("\nTotal de artistas en el rango de " + char + ": " + str(artists[0]))


    elif int(inputs[0]) == 3:
        minEnergy = input("Ingrese la energía minima: ")
        maxEnergy = input("Ingrese la energía maxima: ")
        minDanceability = input("Ingrese la danzabilidad minima: ")
        maxDanceability = input("Ingrese la danzabilidad maxima: ")
        total = controller.getMusicToCelebrate(catalog,minEnergy,maxEnergy,minDanceability,maxDanceability)
        print(total)

    elif int(inputs[0]) == 4:

        minEnergy = input("Ingrese la instrumentalidad minima: ")
        maxEnergy = input("Ingrese la instrumentalidad maxima: ")
        minDanceability = input("Ingrese el tempo minima: ")
        maxDanceability = input("Ingrese el tempo maxima: ")
        total = controller.getMusicToCelebrate1(catalog,minEnergy,maxEnergy,minDanceability,maxDanceability)
        print(total)

    elif int(inputs[0]) == 5:
        printGenres()
        genreTuple = input("Ingrese los numeros de los generos que desea buscar separados por espacios: ")
        genreTuple = genreTuple.split(',')
        genreTuple = tuple(genreTuple)
        for genrePos in genreTuple:
            genrePos = int(genrePos)
            if genrePos <= 0 or genrePos > 10:
                print("Ingrese una numero valido")
            elif genrePos !=10:
                tempoRange = controller.getGenre(genrePos)
                genre = tempoRange[2]
                minTempo = tempoRange[0]
                maxTempo = tempoRange[1]
                total = controller.getCharacteristicByRange(catalog, minTempo, maxTempo, "tempo")
                artists = controller.getArtists(catalog, minTempo, maxTempo, "tempo")
                print("Para "+str(genre)+" el tempo esta entre "+str(minTempo)+" y "+str(maxTempo)+" BPM...")
                print("\nEl numero de reproducciones para este genero fueron: "+str(total))
                print("\nEl numero de artistas para este genero fueron: "+str(artists[0]))
                print("\n Los diez primeros artistas son")
                counter = 0
                while counter < 10:
                    counter = counter + 1
                    print('Artista '+ str(counter) + ' : ' + lt.getElement(artists[1],counter))
                    
               
        
            elif genrePos == 10:
                genre = input("Ingrese el nombre del nuevo genero: ")
                minTempo = float(input("Ingrese el valor minimo del tempo: "))
                maxTempo = float(input("Ingrese el valor maximo del tempo: "))
                total = controller.getCharacteristicByRange(catalog,minTempo,maxTempo, "tempo")
                artists = controller.getArtists(catalog, minTempo, maxTempo, "tempo")
                print("Para "+str(genre)+" el tempo esta entre "+str(minTempo)+" y "+str(maxTempo)+" BPM...")
                print("\nEl numero de reproducciones para este genero fueron: "+str(total))
                print("\nEl numero de artistas para este genero fueron: "+str(artists[0]))
                print("\n Los diez primeros artistas son")
                counter = 0
                while counter < 10:
                    counter = counter + 1
                    print('Artista '+ str(counter) + ' : ' + lt.getElement(artists[1],counter))
                    
    
    elif int(inputs[0]) == 6:
        initialTime = input("Ingrese la hora minima (H:M): ")
        finalTime = input("Ingrese la hora maxima (H:M): ")
        total = controller.getTimeByRange(catalog,initialTime,finalTime)
        print('El genero mas escuchado entre las ' + str(initialTime) + ' y las ' + str(finalTime) + ' es ' + str(total[0]) + ' con ' + str(total[1]) +' reproducciones y un vader promedio de '+ str(total[2]))
        
   

    else:
        sys.exit(0)
sys.exit(0)
