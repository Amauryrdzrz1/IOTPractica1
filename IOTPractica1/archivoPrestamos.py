import csv
from tempfile import NamedTemporaryFile
import shutil

class archivoPrestamos:
    def __init__(self,idprestamo, estudiante, objeto, fechaprestamo, fecharetorno):
        self.idprestamo= idprestamo
        self.estudiante = estudiante
        self.objeto = objeto
        self.fechaprestamo = fechaprestamo
        self.fecharetorno = fecharetorno

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