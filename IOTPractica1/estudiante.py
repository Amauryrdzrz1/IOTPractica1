setsEstudiantes = []
from Archivos import lecturaArchivos as p
import csv

class classEstudiante:
    
    def __init__(self, matricula, nombre, grupo, adeudo):
        self.matricula = matricula
        self.nombre = nombre
        self.grupo = grupo
        self.adeudo = adeudo
    
    def ingresarDatos(self, nombre, grupo):
        obtenIncremental = p(self.matricula, self.nombre, self.grupo, self.adeudo)
        self.matricula = obtenIncremental.obtenerIncremental()
        self.nombre = nombre
        self.grupo = grupo
        self.escribirEstudiantes(self.matricula, self.nombre, self.grupo, self.adeudo)
    
    def actualizaAdeudo(self, matricula, adeudo):
        self.matricula = matricula
        idx = 0
        for estudiante in setsEstudiantes: 
            if estudiante.matricula == self.matricula:
                estudiante.adeudo = adeudo
                est = {
                    "Matricula":estudiante.matricula,
                    "Nombre":estudiante.nombre,
                    "Grupo":estudiante.grupo,
                    "Adeudo":estudiante.adeudo
                    }
                print(est) 
                setsEstudiantes.pop(idx)
                setsEstudiantes.append(classEstudiante(estudiante.matricula, estudiante.nombre, estudiante.grupo, estudiante.adeudo))
            idx = idx + 1

    def verEstudiante(self):
        for estudiante in setsEstudiantes: 
            est = {
                "Matricula":estudiante.matricula,
                "Nombre":estudiante.nombre,
                "Grupo":estudiante.grupo,
                "Adeudo":estudiante.adeudo
                }
            print(est) 
            
    def buscarEstudiante(self, matricula):
        self.matricula = int(input("ingresa la matricula del estudiante: "))
        buscaEstudiante = p(self.matricula,self.nombre,self.grupo,self.adeudo)
        mat = buscaEstudiante.buscarEstudiante(self.matricula)
        return mat;

    def eliminarEstudiante(self, matricula):
        self.matricula = int(input("ingresa la matricula del estudiante a eliminar: "))
        idx = 0
        for estudiante in setsEstudiantes: 
            if estudiante.matricula == self.matricula:
                est = {
                    "Matricula":estudiante.matricula,
                    "Nombre":estudiante.nombre,
                    "Grupo":estudiante.grupo,
                    "Adeudo":estudiante.adeudo
                    }
                print("Estudiante removido...")
                print(est)
                setsEstudiantes.pop(idx)
            idx += 1 

    def escribirEstudiantes(self, matricula, nombre, grupo, adeudo):

        with open('estudiantes.csv', 'a', newline='\n') as file:
            csv_escritor = csv.DictWriter(
                file, fieldnames=['matricula', 'nombre', 'grupo', 'adeudo'])

            if file.tell() == 0:
                csv_escritor.writeheader()

            csv_escritor.writerow({'matricula': matricula,
                               'nombre': nombre,
                               'grupo': grupo,
                               'adeudo': adeudo
                               })
    