from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Establecimiento, Parroquia
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
    
    for x in read:
        # Variable que devuelve la parroquia de cada establecimiento
        aux = session.query(Parroquia).filter_by(codigo = x[6]).first()        
        # Creacion de cada objeto de tipo establecimiento
        est = Establecimiento(codigo = x[0], nombre = x[1], nroDistrito = x[8], sostenimiento = x[9], tipo = x[10]
        , modalidad = x[11], jornada = x[12], acceso = x[13], nroEstudiantes = int(x[14]), nroDocentes = int(x[15]), parroquia = aux)
        session.add(est) 
 
session.commit()