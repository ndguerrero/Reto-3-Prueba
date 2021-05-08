﻿"""
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
 """

import config as cf
import model
import csv
import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadEvents(catalog):
    eventsfile1 = cf.data_dir + "subsamples-small/context_content_features-small.csv"
    eventsDict1 = csv.DictReader(open(eventsfile1, encoding='utf-8'))
    for rep in eventsDict1:
        model.addRep(catalog, rep)

    eventsfile2 = cf.data_dir + "subsamples-small/user_track_hashtag_timestamp-small.csv"
    eventsDict2 = csv.DictReader(open(eventsfile2, encoding='utf-8'))
    for rep in eventsDict2:
        model.addHash(catalog, rep)

    eventsfile3 = cf.data_dir + "subsamples-small/sentiment_values.csv"
    eventsDict3 = csv.DictReader(open(eventsfile3, encoding='utf-8'))
    for rep in eventsDict3:
        model.addFeeling(catalog, rep)
    
    
        


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def repSize(catalog):
   return model.repSize(catalog)

def indexHeight(catalog):
   return model.indexHeight(catalog)

def getCharacteristicByRange(catalog, minChar, maxChar, char):
    return model.getCharacteristicByRange(catalog, minChar, maxChar, char)

def getMusicToCelebrate(catalog,minEnergy,maxEnergy,minDanceability,maxDanceability):
    return model.getMusicToCelebrate(catalog,minEnergy,maxEnergy,minDanceability,maxDanceability)

def getMusicToCelebrate1(catalog,minEnergy,maxEnergy,minDanceability,maxDanceability):
    return model.getMusicToCelebrate1(catalog,minEnergy,maxEnergy,minDanceability,maxDanceability)

def getGenre(genrePos):
    return model.getGenre(genrePos)

def newGenreList():
    return model.newGenreList()

def getTimeByRange(catalog,initialTime,finalTime):
    initialTi = datetime.datetime.strptime(initialTime, '%H:%M')
    initialTi = initialTi.time()
    finalTi = datetime.datetime.strptime(finalTime, '%H:%M')
    finalTi = finalTi.time()
    result = model.getGenreByTimeRange(catalog, initialTi, finalTi)
    return result

def getArtists(catalog, minChar, maxChar, char):
    return model.getArtists(catalog, minChar, maxChar, char)

