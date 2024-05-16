import random
def generarDatosCalidadAire():

    listaDatos=[]
    for i in range(1000):
        nombre=random.choice(['ana perez','santiago vasquez','andres felipe',
        'alejandro sanchez','samuel perez','santiago perez'])
        comuna=random.randint(1,14)
        ica=random.randint(10,80)
        fecha=random.choice(['2024-05-15','2024-0-16','2024-05-17'])
        correo=random.choice(['correo@correo.com','correo@correo.com', 'correo@correo.com',
        'correo@correo.com','correo@correo.com'])

        encuesta =[nombre,comuna,ica,fecha,correo]

        listaDatos.append(encuesta)

    return listaDatos
print(generarDatosCalidadAire())