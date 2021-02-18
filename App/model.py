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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def newCatalog():

    catalog= {'videos': None, 
              'category': None, 
              'country': None}

    catalog['videos'] = lt.newList()
    catalog['category'] = lt.newList('ARRAY_LIST',
                                     cmpfunction=comparecategory)
    return catalog
    
# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):

    lt.addLast(catalog['videos'], video)
    categorias = video['categorias'].split(",")
    for category in categorias:
        addCategory(catalog, category.strip(), video)

def addCategory(catalog, categoria, video):

    categorias = catalog['categorias']
    poscategory = lt.isPresent(categorias, categoria)
    if poscategory > 0:
        category = lt.getElement(categorias, poscategory)
    else:
        category = newCategory(categoria)
        lt.addLast(categorias, category)
    lt.addLast(category['videos'], video)


# Funciones para creacion de datos

def newCategory(name):

    category = {'name': "", "videos": None, "views": 0}
    category['name'] = name
    category['videos'] = lt.newList('ARRAY_LIST')
    return category

# Funciones de consulta

def getVideosByCategory(catalog, categoria):

    poscategory = lt.isPresent(catalog['categorias'], categoria)
    if poscategory > 0:
        category = lt.getElement(catalog['categorias'], poscategory)
        return category
    return None

def getBestVideos(catalog, number):

    videos = catalog['videos']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos

# Funciones utilizadas para comparar elementos dentro de una lista

def compareviews(video1, video2):
    return (float(video1['views']) > float(video2['views']))

def comparecategory(categoria1, category):

    if(categoria1.lower() in category['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento

def sortVideos(catalog):
    sa.sort(catalog['videos'], compareviews)