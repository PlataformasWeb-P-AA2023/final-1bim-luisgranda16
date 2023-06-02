from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

# se importa la clase(s) del archivo genera_tablas
from genera_tablas import *
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos para el ejemplo se usa la base de datos sqlite

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()
# Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores
parroquias = session.query(Canton).join(Parroquia, Establecimiento).filter(Establecimiento.nroDocentes == 0 and Establecimiento.nroDocentes == 5 and Establecimiento.nroDocentes == 11).all()
print("Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores")
for p in parroquias:
    print(p,"\n")

# Establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
cantones = session.query(Establecimiento).join(Parroquia).filter(and_(Parroquia.parroquia == "PINDAL", Establecimiento.nroEstudiantes >= 21)).all()
print("Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21")
for p in cantones:
    print(p,"\n")