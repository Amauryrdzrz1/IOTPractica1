setsEstudiantes = []
from Archivos import *
import csv

class classEstudiante:
    
    def __init__(self, matricula, nombre, grupo, adeudo):
        self.matricula = matricula
        self.nombre = nombre
        self.grupo = grupo
        self.adeudo = adeudo
    
    def ingresarDatos(self, nombre, grupo):
        self.matricula = self.matricula + 1
        self.nombre = input("Ingresar nombre: ")
        self.grupo = input("Ingresar grupo: ")
        setsEstudiantes.append(classEstudiante(self.matricula, self.nombre, self.grupo, None))
        with open('estudiantes.csv', 'a') as f:
            csv_escritor = csv.DictWriter(f, fieldnames =['matricula','nombre','grupo','adeudo'])
            csv_escritor.writeheader()
            csv_escritor.writerow({'matricula':self.matricula,
                                     'nombre':self.nombre,
                                     'grupo':self.grupo,
                                     'adeudo':self.adeudo
                })
        print("El Estudiante ha sido registrado!")

    
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
        for estudiante in setsEstudiantes: 
            if estudiante.matricula == self.matricula:
                est = {
                    "Matricula":estudiante.matricula,
                    "Nombre":estudiante.nombre,
                    "Grupo":estudiante.grupo,
                    "Adeudo":estudiante.adeudo
                    }
                print(est) 
                return estudiante.matricula

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
                