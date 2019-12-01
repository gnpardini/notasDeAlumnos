def pedirLegajoDeAlumno():
    legajo = int(input("Ingrese un legajo de alumno"))
    while ((legajo < 0) and (legajo != -1))or (legajo > 9999999):
        legajo = int(input("Error. Ingrese un legajo válido alumno"))
    return legajo

def pedirPrimerNota():
    nota1 = int(input("Ingrese la primer nota"))
    while (nota1 < 0) or (nota1 > 10):
        nota1 = int(input("Error. Ingrese una nota válida"))
    return nota1

def pedirSegundaNota():
    nota2 = int(input("Ingrese la segunda nota"))
    while (nota2 < 0) or (nota2 > 10):
        nota2 = int(input("Error. Ingrese una nota válida"))
    return nota2

def contarCuantosAlumnosPromocionan(listaDePrimerasNotas,listaDeSegundasNotas,listaDeLegajos):
    primerNota = 0
    segundaNota = 0
    contador = 0
    
    for i in range(len(listaDePrimerasNotas)):
        if (listaDePrimerasNotas [i] >= 7):
            primerNota = listaDePrimerasNotas[i]
            if (listaDeSegundasNotas[i] >= 7):
                segundaNota = listaDeSegundasNotas[i]
                contador = contador + 1
    return contador

def informarAlumnosQuePromocionan(listaDePrimerasNotas,listaDeSegundasNotas,listaDeLegajos):
    primerNota = 0
    segundaNota = 0
    for i in range(len(listaDePrimerasNotas)):
        if (listaDePrimerasNotas [i] >= 7):
            primerNota = listaDePrimerasNotas[i]
            if (listaDeSegundasNotas[i] >= 7):
                segundaNota = listaDeSegundasNotas[i]
                print("El alumno", listaDeLegajos[i]," promociona")
                
            
                
def informarAlumnosQueDebenRendirFinal(listaDePrimerasNotas,listaDeSegundasNotas,listaDeLegajos):
    for i in range(len(listaDePrimerasNotas)):
        if ((listaDePrimerasNotas[i] < 7) and (listaDePrimerasNotas[i] >= 4)) or ((listaDeSegundasNotas[i] < 7) and (listaDeSegundasNotas[i] >= 4)):
            print("El alumno", listaDeLegajos[i],"debe rendir final")
            
def informarAlumnosQueDebenRecuperar(listaDePrimerasNotas,listaDeSegundasNotas,listaDeLegajos):
    for i in range (len(listaDePrimerasNotas)):
        if (listaDePrimerasNotas [i] < 4) and (listaDeSegundasNotas[i] >=4 ):
            print("El alumno", listaDeLegajos[i],"debe recuperar el primer parcial")
        if (listaDeSegundasNotas[i] < 4) and (listaDePrimerasNotas[i] >= 4):
            print("El alumno", listaDeLegajos[i],"debe recuperar el segundo parcial")
        if (listaDePrimerasNotas[i] < 4) and (listaDeSegundasNotas[i] < 4):
            print("El alumno", listaDeLegajos[i], "debe recuperar ambos parciales")
            
            
            
            
    
#Programa principal
listaDeLegajos = []
listaDePrimerasNotas = []
listaDeSegundasNotas = []
legajo = pedirLegajoDeAlumno()
while legajo != -1:
    listaDeLegajos.append(legajo)
    primerNota = pedirPrimerNota()
    listaDePrimerasNotas.append(primerNota)
    segundaNota = pedirSegundaNota()
    listaDeSegundasNotas.append(segundaNota)
    legajo = pedirLegajoDeAlumno()
cantidadDeAlumnosQuePromocionan = contarCuantosAlumnosPromocionan(listaDePrimerasNotas,listaDeSegundasNotas,listaDeLegajos)
informarAlumnosQuePromocionan(listaDePrimerasNotas,listaDeSegundasNotas,listaDeLegajos)
informarAlumnosQueDebenRendirFinal(listaDePrimerasNotas,listaDeSegundasNotas,listaDeLegajos)
informarAlumnosQueDebenRecuperar(listaDePrimerasNotas,listaDeSegundasNotas,listaDeLegajos)
if cantidadDeAlumnosQuePromocionan == 0:
    print("No promocionó ningún alumno")
    