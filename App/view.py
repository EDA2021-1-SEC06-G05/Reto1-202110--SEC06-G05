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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Seleccionar el tipo de representación de la lista")
    print("2- Consultar el TOP n de tendencias por categoria y pais")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printCategoryData(category):
    if category:
        print('categoria encontrada:' + category['name'])
        print('Reproducciones' + str(category['views']))
        print('Total de videos:' + str(lt.size(category['videos'])))
        for videos in lt.iterator(category['videos']):
            print('Titulo:' + video['title'] + 'Nombre del canal:' + video['channel_title'])
        else:
            print('No se encontro la categoria')

def printBestVideos(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores videos:')
        for video in lt.iterator(videos):
            print('Titulo:' + video['title'] + 'Fecha de tendencia:' + video['trending_date'] + 
                  'Nombre del canal:' + video['channel_title'] + 'Fecha de publicacion:' + 
                  video['publish_time'] + 'Reproducciones:' + video['views'] + 'Likes:' + 
                  video['likes'] + 'Dislikes:' + video['dislikes'] )
    else:
        print('No se encontraron videos')        

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        size = input('(1) para ARRAY_LIST o (2) para LINKED_LIST\n : ')
        if int(size[0])==1:
            print("Cargando información de los archivos en ARRAY_LIST....")
            catalog = initCatalog()
            loadData(catalog)
            print('Videos cargados:' + str(lt.size(catalog['videos'])))
            print('Canales cargados' + str(lt.size(catalog['channel'])))
            print('Paises cargados' + str(lt.size(catalog['country'])))
            print('Categorias cargadas' + str(lt.size(catalog['category'])))
        elif int(size[0])==2:    
            print("Cargando informacion de los archivos en LINKED_LIST")



        result = controller.sortBooks(catalog, int(size))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0]))
        printResults(result[1])
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados:' + str(lt.size(catalog['videos'])))
        print('Canales cargados' + str(lt.size(catalog['channel'])))
        print('Paises cargados' + str(lt.size(catalog['country'])))
        print('Categorias cargadas' + str(lt.size(catalog['category'])))
    elif int(inputs[0]) == 3:
        number = input("Buscando los TOP ?:")
        videos = controller.getBestVideos(catalog, int(number))
        printBestVideos(videos)
    else:
        sys.exit(0)
sys.exit(0)
