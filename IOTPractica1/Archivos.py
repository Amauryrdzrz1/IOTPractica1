import csv
class lecturaArchivos:
    def __init__(self,matricula,nombre,grupo,adeudo):
        self.matricula = matricula
        self.nombre = nombre
        self.grupo = grupo
        self.adeudo = adeudo

    def verEstudiantes(self):
        with open('estudiantes.csv', 'r') as estudiantesCsv:
            lectorCsv = csv.DictReader(estudiantesCsv)

            for linea in lectorCsv:
                print(linea)

    def escribirEstudiantes(self,matricula, nombre, grupo, adeudo):
        self.matricula = matricula
        self.nombre = nombre
        self.grupo = grupo
        self.adeudo = adeudo

    #def verObjetos(self):