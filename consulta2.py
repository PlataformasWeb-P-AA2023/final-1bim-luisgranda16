from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from genera_tablas import *
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos para el ejemplo se usa la base de datos sqlite

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
# Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
parroquias = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada == 'Matutina y Vespertina').all()
print("Las parroquias que tienen establecimientos únicamente en la jornada Matutina y Vespertina.")
for p in parroquias:
    print(p,"\n")


# Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
cantones = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.nroEstudiantes == 448 , 
    Establecimiento.nroEstudiantes == 450,
    Establecimiento.nroEstudiantes == 451,
    Establecimiento.nroEstudiantes == 454,
    Establecimiento.nroEstudiantes == 458,
    Establecimiento.nroEstudiantes == 459
    )).all()
# Impresion de los valores obtenidos
print("Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459")
for p in cantones:
    print(p,"\n")