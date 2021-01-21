from datetime import date
from estudiante import classEstudiante as e
from objeto import classObjeto as o
from prestamoRetorno import classPrestamo as p
from Archivos import lecturaArchivos as v
from archivoObjetos import archivoObjetos as arco
x=0
claveobj = 0
matricula = 0
idprestamo = 0
nombre = ""
grupo = ""
adeudo = False
debe = False
fechaP= date.today()
fechaE= date.today()
print(fechaP)
estud = e(matricula,nombre, grupo,adeudo)
objet = o(claveobj,nombre)
prestamo = p(idprestamo,estud,objet,fechaP,fechaE)
verestudiantes = v(matricula,nombre,grupo,adeudo)
archo = arco(claveobj,nombre)

while x!=9:
  print("~~Menu~~");
  print("1.- Registrar estudiante");
  print("2.- Registrar objeto");
  print("3.- Registrar prestamo de objeto");
  print("4.- Registrar retorno de objeto");
  print("5.- Ver estudiantes");
  print("6.- Ver objetos");
  print("7.- Ver Prestamos");
  print("8.- eliminar usuario/objeto");
  print("9.- Salir");
  x=int(input("Selecciona una opcion: "));
  if x == 1:
    nombre = input("escribe el nombre del estudiante: ")
    grupo = input("escribe el grupo: ")
    estud.ingresarDatos(nombre,grupo)

  elif x == 2:
    nombre = input("escribe el nombre del objeto a registrar: ")
    objet.ingresarObjeto(nombre)

  elif x == 3:
    matricula = estud.buscarEstudiante(matricula)
    if matricula != None:
        debe = prestamo.validaEstudiante(matricula)
        if debe == False:
            objeto = objet.buscarObjeto(claveobj)
            if objeto != None:
                prestamo.hacerPrestamo(matricula,objeto,date.today(),None)
                estud.actualizaAdeudo(matricula,adeudo)
            else:
                print("no se ha encontrado el objeto")
        else: 
            print("estudiante con adeudo")
    else:
        print("no se ha encontrado al estudiante")

  elif x == 4:
      matricula = prestamo.hacerRetorno(idprestamo,date.today())
      if matricula != None:
          estud.actualizaAdeudo(matricula,False)

  elif x == 5:
    estud.verEstudiante()
    verestudiantes.verEstudiantes()

  elif x == 6:
    #objet.verObjeto()
    archo.verObjetos()

  elif x == 7:
      prestamo.verPrestamos()

  elif x == 8:
      a = ''
      b = ''
      print("Desea eliminar el registro de un estudiante?")
      a = input("y/n: ")
      if a == 'y':
        estud.eliminarEstudiante(matricula)
      else:  
        print("Desea eliminar un objeto?")
        b = input("y/n: ")
        if a == 'y':
            objet.eliminarObjeto(claveobj)
        else:
            print("Regresando al menu...")
  
           