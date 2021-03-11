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
import operator 
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def newCatalog(tipoEstructura):
    catalog= {'videos': None, 'category': None, "views": None, "title": None}

    catalog['videos'] = lt.newList(datastructure=tipoEstructura)
    catalog['category'] = lt.newList(datastructure=tipoEstructura)
    catalog["views"] = lt.newList(datastructure= tipoEstructura, cmpfunction= cmpVideosByViews)
    catalog["title"] = lt.newList(datastructure= tipoEstructura)
    return catalog
    
# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    lt.addLast(catalog["views"],video)    
    lt.addLast(catalog["title"], video)

def addCategory(catalog, categoria):
    categorias = catalog["category"] 
    lt.addLast(categorias, categoria) 


# Funciones para creacion de datos

def newCategory(name):
    category = {'name': "", "videos": None, "views": 0}
    category['name'] = name
    category['videos'] = lt.newList('ARRAY_LIST')
    return category

# Funciones de consulta
def crearSubLista(catalog, muestra):
    nuevaLista = lt.subList(catalog["videos"], 1, muestra)

    return nuevaLista

def crearSubLista2(catalog, muestra):
    nuevaLista2 = lt.subList(catalog["category"], 1, muestra)
    return nuevaLista2

def ejemplo(catalog, muestra):
    ejemplo = lt.subList(catalog["title"], 1, muestra)
    return ejemplo

def req4(pais, idCategoria, catalog):
    nuevaListaVideos = catalog["videos"]
    listaFinal = lt.newList()
    for i in range (1, lt.size(nuevaListaVideos)):
        video = lt.getElement(nuevaListaVideos, i)
        if(video["category_id"] == idCategoria and video["country"] == pais):
            lt.addLast(listaFinal, video)
    return listaFinal

def getVideosByCategory(catalog, categoria):

    poscategory = lt.isPresent(catalog['category'], categoria)
    if poscategory > 0:
        category = lt.getElement(catalog['category'], poscategory)
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

def estudianteA(catalog, pais):
    listaVideos = catalog["videos"]
    dicRes = {}
    for i in range (1, lt.size(listaVideos)): 
        video = lt.getElement(listaVideos, i)
        if(pais == video["country"]):
            if (video["title"] in dicRes):
                dicRes[video["title"]]+=1 
            else:
                dicRes[video["title"]]=1    
    sortVideos = sorted(dicRes.items(), key= operator.itemgetter(1), reverse= True)
    trendingVideo = sortVideos[0][0]
    contadorDias = sortVideos[0][1]
    for i in range (1, lt.size(listaVideos)):
        video = lt.getElement(listaVideos, i)
        if(trendingVideo == video["title"]):

            return video, contadorDias

def estudianteB(catalog, idCategoria):
    listaVideos = catalog["videos"]
    dicRes = {}
    for i in range (1, lt.size(listaVideos)): 
        video = lt.getElement(listaVideos, i)
        if(idCategoria == video["category_id"]):
            if (video["title"] in dicRes):
                dicRes[video["title"]]+=1 
            else:
                dicRes[video["title"]]=1    
    sortVideos = sorted(dicRes.items(), key= operator.itemgetter(1), reverse= True)
    trendingVideo = sortVideos[0][0]
    contadorDias = sortVideos[0][1]
    for i in range (1, lt.size(listaVideos)):
        video = lt.getElement(listaVideos, i)
        if(trendingVideo == video["title"]):

            return video, contadorDias

def compareviews(video1, video2):
    return (float(video1['views']) > float(video2['views']))


def comparelikes(video1, video2):
    return (float(video1['likes']) > float(video2['likes']))
 

def req10(catalog, numeroVideos, pais, tag):
    nueva = lt.newList()
    nueva.shellVideosLikes(catalog)
    for i in range (1, lt.size(nueva)):
        video = lt.getElement(nueva, i)
        if(pais == video["country"] and "" ""+tag+"" "" in video['tags'].split('|')):
            lt.addLast(nueva, video)
    return nueva(catalog, numeroVideos, pais, tag)      

def comparecategory(categoria1, category):

    if(categoria1.lower() in category['name'].lower()):
        return 0
    return -1

def cmpVideosByViews(video1, video2):
    
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    views1 = False
    print(float(video2['views']), float(video1['views']))
    if (float(video2['views'])) > (float(video1['views'])):
        views1 = True
    return views1   

# Funciones de ordenamiento

def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        return lt.subList(lst, pos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')

def sortVideos(catalog):
    sa.sort(catalog['videos'], compareviews)

def sortVideosLikes(catalog):
    sa.sort(catalog["videos"],comparelikes)
    
def selectionVideos(catalog):
    sel.sort(catalog['videos'], compareviews)
    
def insertionVideos(catalog):    
    ins.sort(catalog["videos"], compareviews)

def shellVideos(catalog):
    shell.sort(catalog, compareviews)

def shellVideosLikes(catalog):
    shell.sort(catalog["videos"], comparelikes)

def quickVideos(catalog):
    quick.sort(catalog["videos"],compareviews)

def mergeVideos(catalog):
    merge.sort(catalog["videos"], compareviews)    