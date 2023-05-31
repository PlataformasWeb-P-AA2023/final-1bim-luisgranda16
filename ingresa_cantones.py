from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Canton, Provincia
from configuracion import cadena_base_datos

import csv

# se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de datos
with open("data/Listado-Instituciones-Educativas.csv", "r", encoding='utf-8') as File:
    # Separar cada columna del CSV
    read = csv.reader(File, delimiter='|')
    # Salto del encabezado del csv
    next(read)
    # Lista que guardara cada linea del CSV
    listaC = []
    for x in read:
        #Almacenamiento de las columnas que nos sirven (Codigo de provincia, codigo canton y canton)
        auxCanton = x[2] + "|" + x[4] + "|" + x[5]
        # Agregar la variable anterior a la lista
        listaC.append(auxCanton)
    # Eliminar duplicados de la lista
    listaC = list(set(listaC))

    
    for x in listaC:
        # Variable que devuelve la provincia de cada canton
        aux = session.query(Provincia).filter_by(codigo = x.split("|")[0]).first()
        # Creacion de cada objeto de tipo canton
        cant = Canton(codigo = x.split("|")[1], canton = x.split("|")[2], provincia = aux)
        # Agregar a la base el canton
        session.add(cant)

session.commit()