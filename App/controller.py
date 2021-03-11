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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(parametro):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(parametro)
    return catalog

# Funciones para la carga de datos

def crearSubLista(catalog, muestra):
    nuevaLista = model.crearSubLista(catalog, muestra)
    return nuevaLista

def req4( pais, idCategoria, catalog):
    return model.req4( pais, idCategoria, catalog)

def req10(catalog, numeroVideos, pais, tag):
    return model.req10(catalog, numeroVideos, pais, tag)

def estudianteA(catalog, pais):
    return model.estudianteA(catalog,pais)

def estudianteB(catalog, idCategoria):
    return model.estudianteB(catalog, idCategoria) 

def crearSubLista2(catalog, muestra):
    nuevaLista2 = model.crearSubLista2(catalog, muestra)
    return nuevaLista2

def ejemplo(catalog, muestra):
    nejemplo = model.ejemplo(catalog, muestra)
    return nejemplo

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategory(catalog)

def loadVideos(catalog):
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategory(catalog):
    categoryfile = cf.data_dir + 'category-id.csv'
    dialect= csv.excel()
    dialect.delimiter="\t"
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'), dialect= dialect)
    for category in input_file:
        model.addCategory(catalog, category) 

# Funciones de ordenamiento

def sortVideos(catalog):
    model.sortVideos(catalog)

def selectionVideos(catalog):
    model.selectionVideos(catalog)

def insertionVideos(catalog):
    model.insertionVideos(catalog)   

def shellVideos(catalog):
    model.shellVideos(catalog)       
    
def quickVideos(catalog):
    model.quickVideos(catalog)

def mergeVideos(catalog):
    model.mergeVideos(catalog)        

# Funciones de consulta sobre el catálogo

def getVideosByCategory(catalog, categoria):

    category = model.getVideosByCategory(catalog, categoria)
    return category

def getBestVideos(catalog, number):

    bestvideos = model.getBestVideos(catalog, number)
    return bestvideos