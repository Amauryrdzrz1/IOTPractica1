import csv
from tempfile import NamedTemporaryFile
import shutil

class lecturaArchivos:
    def __init__(self,matricula,nombre,grupo,adeudo):
        self.matricula = matricula
        self.nombre = nombre
        self.grupo = grupo
        self.adeudo = adeudo
        
        #
                    
    def verEstudiantes(self):
        with open('estudiantes.csv', 'r') as estudiantesCsv:
            lectorCsv = csv.DictReader(estudiantesCsv)

            for linea in lectorCsv:
                print(linea)

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
    
    def buscarEstudiante(self,matricula):
        filename = 'estudiantes.csv'
        clave = None
        with open(filename,'r') as file:
            csv_reader = csv.DictReader(file, fieldnames = ['matricula', 'nombre'])
            for row in csv_reader:
                if row['matricula']  == str(matricula):
                    clave = matricula
        return clave

    def cambiarAdeudo(self, matricula):
        tempfile = NamedTemporaryFile(mode='w', delete = False,encoding='utf8', newline='')
        filename = 'estudiantes.csv'
        matriculaEncontrada = None
        with open(filename,'r') as file, tempfile:
            csv_reader = csv.DictReader(file, fieldnames = ['matricula', 'nombre', 'grupo', 'adeudo'])
            writer = csv.DictWriter(tempfile, fieldnames = ['matricula', 'nombre', 'grupo', 'adeudo'])
            
            for row in csv_reader:
                if row['matricula']  == str(matricula):
                    print('matricula a actualizar->',row['matricula'])
                    row['adeudo'] = False
                    matriculaEncontrada = matricula
                row = {'matricula': row['matricula'], 'nombre': row['nombre'], 'grupo': row['grupo'], 'adeudo': row['adeudo']}
                writer.writerow(row)

        shutil.move(tempfile.name, filename)

        return matriculaEncontrada;

    def obtenerIncremental(self):
        id_file = 0
        with open('incremental.csv','r') as arc: 
            csv_reader = csv.DictReader(arc)
            for row in csv_reader:
                for (i,v) in row.items():
                    if i == 'id':
                       id_file = int(v) + 1
                    else:
                       id_file = 1;
        with open('incremental.csv', 'w') as file:
            csv_escritor = csv.DictWriter(
                file, fieldnames=['id'])
            csv_escritor.writeheader()
            csv_escritor.writerow({'id': id_file});
            return id_file;
        
    def hizoPrestamo(self,matricula):
        tempfile = NamedTemporaryFile(mode='w', delete = False,encoding='utf8', newline='')
        filename = 'estudiantes.csv'
        matriculaEncontrada = None
        with open(filename,'r') as file, tempfile:
            csv_reader = csv.DictReader(file, fieldnames = ['matricula', 'nombre', 'grupo', 'adeudo'])
            writer = csv.DictWriter(tempfile, fieldnames = ['matricula', 'nombre', 'grupo', 'adeudo'])
            
            for row in csv_reader:
                if row['matricula']  == str(matricula):
                    print('matricula a actualizar->',row['matricula'])
                    row['adeudo'] = True
                    matriculaEncontrada = matricula
                row = {'matricula': row['matricula'], 'nombre': row['nombre'], 'grupo': row['grupo'], 'adeudo': row['adeudo']}
                writer.writerow(row)

        shutil.move(tempfile.name, filename)