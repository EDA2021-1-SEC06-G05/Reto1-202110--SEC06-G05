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
 * but WITHOUT ANY WARRANTY; without even the implied warranty ofU
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import time
import sys
from DISClib.ADT import list as lt
from datetime import datetime
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
"""st
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Seleccionar el tipo de representación de la lista donde se cargaran los datos")
    print("2- Seleccione el tipo de algoritmo de ordenamiento iterativo")
    print("3- Cuál es el video que más días ha sido trending en un pais")
    print("4- Cuál es el video que más días ha sido trending de una categoria dada")
    print("5- Conocer los videos con mas views de una categoria")
    print("6- Conocer el numero de videos con mas likes de un pais y un tag ")
    print("0- Salir")

def initCatalog(parametro):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(parametro)

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
        for video in lt.iterator(category['videos']):
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
            catalog = initCatalog("ARRAY_LIST")
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
            print('Categorias cargadas: ' + str(lt.size(catalog['category'])))
            print('views cargadas: ' + str(lt.size(catalog['views'])))
            print("Informacion del primer video cargado:\n ")
            print("    Title,             Cannel_title,   trending_date,    country,    views,    likes,   dislikes. ")
            print("nicht mehr lang 🌈,     Dagi Bee,        18.18.05,       germany,   1015471,  42230,    10764 \n " )
           # muestra1 = controller.crearSubLista(catalog, int(1))
           # print(muestra1)
            print("Lista de las categorias:\n ")
            muestra2 = controller.crearSubLista2(catalog, int(32))
            for i in range (1, lt.size(muestra2)): 
                a = lt.getElement(muestra2, i)
                print(a["id"], a["name"])
        elif int(size[0])==2:    
            print("Cargando informacion de los archivos en LINKED_LIST")
            catalog = initCatalog("LINKED_LIST")
            loadData(catalog)
            print('Videos cargados:' + str(lt.size(catalog['videos'])))
            print('Categorias cargadas' + str(lt.size(catalog['category'])))       
            print('views cargadas' + str(lt.size(catalog['views'])))               
            print("Informacion del primer video cargado:\n ")
            print("    Title,           Cannel_title,   trending_date,    country,    views,    likes,   dislikes. ")
            print("nicht mehr lang 🌈,   Dagi Bee,        18.18.05,       germany,   1015471,  42230,    10764 \n " )
            print("Lista de las categorias:\n ")
            muestra2 = controller.crearSubLista2(catalog, int(32))
            print(muestra2)
    elif int(inputs[0]) == 2:
        size = input('(1) para selection, (2) para insertion, (3) para shell, (4) para merge y (5) para quick\n : ')
        pre = input("Cantidad de la muestra : ")
        if int(size[0])==1:
            instanteInicial = datetime.now()
            print("Ordenando por Selection")
            controller.selectionVideos(catalog)
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.microseconds
            print("El tiempo en milisegundos es :")
            print(segundos/1000)
        elif int(size[0])==2:
            instanteInicial = datetime.now()
            print("Ordenando por Insertion")
            controller.insertionVideos(catalog)
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.microseconds
            print("El tiempo en milisegundos es :")
            print(segundos/1000)
        elif int(size[0])==3:
            instanteInicial = datetime.now()
            print("Ordenando por shell")  
            controller.shellVideos(catalog)
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.microseconds
            print("El tiempo en milisegundos es :")
            print(segundos/1000)
        elif int(size[0])==4:
            instanteInicial = datetime.now()
            print("Ordenando por merge")  
            controller.mergeVideos(catalog)
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.microseconds
            print("El tiempo en milisegundos es :")
            print(segundos/1000)  
        elif int(size[0])==5:
            instanteInicial = datetime.now()
            print("Ordenando por quick")  
            controller.quickVideos(catalog)  
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.microseconds
            print("El tiempo en milisegundos es :")
            print(segundos/1000)      

    elif int(inputs[0]) == 3:
        pais = input("Digite el pais ")
        retorno = controller.estudianteA(catalog, pais)
        print('Title:', retorno[0]["title"])
        print('Channel_title:' , retorno[0]["channel_title"])
        print('Country:' , retorno[0]["country"])
        print('Dias:', retorno[1])

    elif int(inputs[0]) == 4:
        idCategoria = input("Digite la categoria ")
        retorno = controller.estudianteB(catalog, idCategoria)
        print('Title:', retorno[0]["title"])
        print('Channel_title:' , retorno[0]["channel_title"])
        print('Category_id:' , retorno[0]["category_id"])
        print('Dias:', retorno[1])
    
    elif int(inputs[0]) == 5:
        numeroVideos = input('Digite el numero de videos que quiere listar \n : ')
        idCategoria = input("Digite el id de la categoria a mostrar en el top \n : ")
        pais = input("digite el pais \n : ")
        req4 = controller.req4( pais, idCategoria, catalog)
        controller.shellVideos(req4) 
        muestra = controller.crearSubLista(catalog, int(numeroVideos))
        for i in range (1, lt.size(muestra)):
            a = lt.getElement(muestra, i)  
            print("title: ", a["title"])
            print("channel_title: ", a["channel_title"])
            print("publish_time:  ", a["publish_time"])
            print("trending_date:  ", a["trending_date"])
            print("views: ", a["views"]) 
            print("likes: ", a["likes"])
            print("dislikes: ", a["dislikes"])

    elif int(inputs[0]) == 6:     
        numeroVideos = input("Digite el numero de videos que quiere listar \n: ")
        pais = input("Digite el pais \n: ")
        tag = input("Digite el tag \n: ")
        req10 = controller.req10(catalog, numeroVideos, pais, tag)
        for i in range(1, lt.size(numeroVideos)):
            a = lt.getElement(numeroVideos, i)
            print("hola")

    else:
        sys.exit(0)
sys.exit(0)