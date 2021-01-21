import csv
from tempfile import NamedTemporaryFile
import shutil

class archivoObjetos:
    def __init__(self,claveObjeto,nombre):
        self.claveObjeto = claveObjeto
        self.nombre = nombre

    def verObjetos(self):
        with open('objetos.csv', 'r') as file:
            lectorCsv = csv.DictReader(file)

            for linea in lectorCsv:
                print(linea)
    
    def escribirObjetos(self,claveObjeto,nombre):

        with open('objetos.csv', 'a', newline='\n') as file:
            csv_escritor = csv.DictWriter(file, fieldnames=['claveObjeto', 'nombre'])

            if file.tell() == 0:
                csv_escritor.writeheader()

            csv_escritor.writerow({'claveObjeto': claveObjeto,
                               'nombre': nombre,
                               })
    
    def buscarObjeto(self,claveObjeto):
        filename = 'objetos.csv'
        with open(filename,'r') as file:
            csv_reader = csv.DictReader(file, fieldnames = ['claveObjeto', 'nombre'])
            for row in csv_reader:
                if row['claveObjeto']  == str(claveObjeto):
                    print(row)
    
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


