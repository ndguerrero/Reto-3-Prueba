"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
import datetime


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {"reps":None,
                "instrumentalness":None,
                "characteristics":None,}

    catalog["reps"] = lt.newList(datastructure = "SINGLE_LINKED")
    catalog["instrumentalness"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["liveness"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["speechiness"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["danceability"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["valence"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["loudness"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["tempo"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["acousticness"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["energy"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["mode"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog["key"]= om.newMap(omaptype='RBT',comparefunction = compareCharacteristics)
    catalog['time'] = om.newMap(omaptype='RBT',comparefunction = compareTimes)

    catalog["hash"] = mp.newMap(numelements=40000, prime=20011, maptype="CHAINING", loadfactor = 2.0, comparefunction=cmpUserId)
    catalog["feeling"] = mp.newMap(numelements=40000, prime=20011, maptype="CHAINING", loadfactor = 2.0)
    


    return catalog

# Funciones para agregar informacion al catalogo

def addRep(catalog, rep):
    lt.addLast(catalog["reps"], rep)
    updateCharacteristic(catalog["instrumentalness"],rep, rep["instrumentalness"])
    updateCharacteristic(catalog["liveness"],rep, rep["liveness"])
    updateCharacteristic(catalog["speechiness"],rep, rep["speechiness"])
    updateCharacteristic(catalog["danceability"],rep, rep["danceability"])
    updateCharacteristic(catalog["valence"],rep, rep["valence"])
    updateCharacteristic(catalog["loudness"],rep, rep["loudness"])
    updateCharacteristic(catalog["tempo"],rep, rep["tempo"])
    updateCharacteristic(catalog["acousticness"],rep, rep["acousticness"])
    updateCharacteristic(catalog["energy"],rep, rep["energy"])
    updateCharacteristic(catalog["mode"],rep, rep["mode"])
    updateCharacteristic(catalog["key"],rep, rep["key"])
    updateTimes(catalog["time"], rep)
    

def updateCharacteristic(map, rep, char):
    repCharacteristic = char
    entry = om.get(map,char)
    if (entry is None):
        dataentry = lt.newList("SINGLE_LINKED")
        om.put(map, repCharacteristic, dataentry)
    else:
        dataentry = me.getValue(entry)
    lt.addLast(dataentry,rep)
    return map

def updateTimes(map, rep):
    repOccuredOn = rep['created_at']
    repDate = datetime.datetime.strptime(repOccuredOn, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map,repDate.time())
    if (entry is None):
        dataentry = lt.newList("SINGLE_LINKED")
        om.put(map, repDate.time(), dataentry)
    else:
        dataentry = me.getValue(entry)
    lt.addLast(dataentry,rep)
    return map

def addHash(catalog, rep):
    existsEntry = mp.get(catalog["hash"], rep["user_id"])
    if existsEntry == None:
        dataentry = lt.newList("SINGLE_LINKED")
        mp.put(catalog["hash"],rep["user_id"],dataentry)
    else:
        dataentry = me.getValue(existsEntry)
    lt.addLast(dataentry, rep)

def addFeeling(catalog, rep):
    existsEntry = mp.get(catalog["feeling"], rep["hashtag"])
    if existsEntry == None:
        dataentry = lt.newList("SINGLE_LINKED")
        mp.put(catalog["feeling"],rep["hashtag"],dataentry)
    else:
        dataentry = me.getValue(existsEntry)
    lt.addLast(dataentry, rep)


# Funciones para creacion de datos

def newGenreList():
    genreList = lt.newList(datastructure="ARRAY_LIST")
    reggae = (60.0,90.0,"Reggae")
    downTempo = (70.0,100.0,"Down-Tempo")
    chillOut = (90.0,120.0,"Chill-out")

    hipHop = (85.0,115.0,"Hip-hop")
    JazzAndFunk = (120.0,125.0,"Jazz and Funk")
    pop = (100.0,130.0,"Pop")

    RnB = (60.0,80.0,"R&B")
    rock = (110.0,140.0,"Rock")
    metal = (100.0,160.0,"Metal")

    lt.addLast(genreList, reggae )
    lt.addLast(genreList, downTempo)
    lt.addLast(genreList, chillOut)
    lt.addLast(genreList, hipHop)
    lt.addLast(genreList, JazzAndFunk)
    lt.addLast(genreList, pop)
    lt.addLast(genreList, RnB)
    lt.addLast(genreList, rock)
    lt.addLast(genreList, metal)
    return genreList

def newGenreList1():
    genreList = lt.newList(datastructure="ARRAY_LIST")
    reggae = {'mini': 60.0, 'maxi': 90.0, 'name': "Reggae", 'reps': 0, 'avg': 0}
    downTempo = {'mini':70.0, 'maxi':100.0,'name':"Down-Tempo",'reps': 0, 'avg': 0}
    chillOut = {'mini':90.0, 'maxi':120.0,'name':"Chill-out",'reps': 0, 'avg': 0}

    hipHop = {'mini':85.0, 'maxi':115.0,'name':"Hip-hop",'reps': 0, 'avg': 0}
    JazzAndFunk = {'mini':120.0, 'maxi':125.0,'name':"Jazz and Funk",'reps': 0, 'avg': 0}
    pop = {'mini':100.0, 'maxi':130.0,'name':"Pop",'reps': 0, 'avg': 0}

    RnB = {'mini':60.0, 'maxi':80.0,'name':"R&B",'reps': 0, 'avg': 0}
    rock = {'mini':110.0, 'maxi':140.0,'name':"Rock",'reps': 0, 'avg': 0}
    metal = {'mini':100.0, 'maxi':160.0,'name':"Metal",'reps': 0, 'avg': 0}

    lt.addLast(genreList, reggae )
    lt.addLast(genreList, downTempo)
    lt.addLast(genreList, chillOut)
    lt.addLast(genreList, hipHop)
    lt.addLast(genreList, JazzAndFunk)
    lt.addLast(genreList, pop)
    lt.addLast(genreList, RnB)
    lt.addLast(genreList, rock)
    lt.addLast(genreList, metal)
    return genreList


# Funciones de consulta

def repSize(catalog):
    return lt.size(catalog["reps"])


def indexHeight(catalog):
    return om.height(catalog["instrumentalness"])


def getGenre(genrePos):
    genreList = newGenreList()
    tempoRange = lt.getElement(genreList,genrePos)
    return tempoRange


def getCharacteristicByRange(catalog, minChar, maxChar, char):
    lst = om.values(catalog[char], minChar, maxChar)
    totreps = 0
    for lstrep in lt.iterator(lst):
        totreps += lt.size(lstrep)
    return totreps

def getArtists(catalog, minChar, maxChar, char):
    lst = om.values(catalog[char], minChar, maxChar)
    lst1 = lt.newList(datastructure='SINGLE-LINKED')
    for element in lt.iterator(lst):
       for element1 in lt.iterator(element):
           if lt.isPresent(lst1,(element1['artist_id'])) == 0:
               lt.addLast(lst1,(element1['artist_id']))

    return lt.size(lst1), lst1



def getMusicToCelebrate(catalog,minEnergy,maxEnergy,minDanceability,maxDanceability):
    lst1 = om.values(catalog["energy"], minEnergy, maxEnergy)
    lst2 = om.values(catalog["danceability"], minDanceability, maxDanceability)
    lst3 = lt.newList(datastructure="SINGLE_LINKED")
    lst4 = lt.newList(datastructure="SINGLE_LINKED")
    finalLst = lt.newList(datastructure="SINGLE_LINKED")

    for element1 in lt.iterator(lst1):
        for element in lt.iterator(element1):
            lt.addLast(lst3,element) 

    for element1 in lt.iterator(lst2):
        for element in lt.iterator(element1):
            lt.addLast(lst4,element)

    for element in lt.iterator(lst3):
        if lt.isPresent(lst4, element):
            lt.addLast(finalLst, element)

    return lt.size(finalList)

def getMusicToCelebrate1(catalog,minEnergy,maxEnergy,minDanceability,maxDanceability):
    lst1 = om.values(catalog["instrumentalness"], minEnergy, maxEnergy)
    lst2 = om.values(catalog["tempo"], minDanceability, maxDanceability)
    lst3 = lt.newList(datastructure="SINGLE_LINKED")
    lst4 = lt.newList(datastructure="SINGLE_LINKED")
    finalLst = lt.newList(datastructure="SINGLE_LINKED")

    for element1 in lt.iterator(lst1):
        for element in lt.iterator(element1):
            lt.addLast(lst3,element) 

    for element1 in lt.iterator(lst2):
        for element in lt.iterator(element1):
            lt.addLast(lst4,element)

    for element in lt.iterator(lst3):
        if lt.isPresent(lst4, element):
            lt.addLast(finalLst, element)

    return lt.size(finalLst)


def getGenreByTimeRange(catalog, initialTi, finalTi):
    lst = om.values(catalog['time'], initialTi, finalTi)
    genreList = newGenreList1()
    for lstrep in lt.iterator(lst):
        for lstrep1 in lt.iterator(lstrep):
            valueHash = me.getValue(mp.get(catalog['hash'], lstrep1['user_id']))
            feel = 0
            for rep in lt.iterator(valueHash):
                if(rep["track_id"]==lstrep1["track_id"] and rep["created_at"]==lstrep1["created_at"]):
                    senti = mp.get(catalog['feeling'], rep['hashtag'])
                    if senti != None:
                        senti = me.getValue(senti)
                        for rep in lt.iterator(senti):
                            if rep['vader_avg'] != '':
                              feel = float(rep['vader_avg'])
                              break
                       
                    
            for genre in lt.iterator(genreList):
                if (float(lstrep1['tempo']) >= float(genre['mini']) and float(lstrep1 ['tempo']) <= float(genre['maxi'])):
                    genre['reps'] =  genre['reps'] + 1
                    genre['avg'] =  genre['avg'] + feel

    maxReps = 0
    maxName = None
    vader = 0

    for genre in lt.iterator(genreList):
        if genre['reps'] > maxReps:
            maxReps = genre['reps']
            maxName = genre['name']
            vader = (genre['avg']/genre['reps'])

    return maxName,  maxReps,  vader



# Funciones utilizadas para comparar elementos dentro de una lista

def compareCharacteristics(char1, char2):
    if (float(char1) == float(char2)):
        return 0
    elif float(char1) > float(char2):
        return 1
    else:
        return -1

def compareTimes(time1, time2):
    if (time1 == time2):
        return 0
    elif (time1 > time2):
        return 1
    else:
        return -1

def cmpUserId(id1,entry):
    identry = me.getKey(entry)
    if (int(id1) == int(identry)):
        return 0
    elif (int(id1) > int(identry)):
        return 1
    else:
        return -1

# Funciones de ordenamiento

