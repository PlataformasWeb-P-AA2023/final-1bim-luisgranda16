from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Parroquia, Canton
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
    listaP = []
    for x in read:
        #Almacenamiento de las columnas que nos sirven (Codigo de canton, codigo parroquia y parroquia)
        auxParroquia = x[4] + "|" + x[6] + "|" + x[7]
        # Agregar la variable anterior a la lista
        listaP.append(auxParroquia)
    # Eliminar duplicados de la lista
    listaP = list(set(listaP))

    for x in listaP:
        # Variable que devuelve la provincia de cada canton
        aux = session.query(Canton).filter_by(codigo = x.split("|")[0]).first()
        # Creacion de cada objeto de tipo canton
        cant = Parroquia(codigo = x.split("|")[1], parroquia = x.split("|")[2], canton = aux)
        session.add(cant)

session.commit()