import csv
from archivoPrestamos import archivoPrestamos as archi
from tempfile import NamedTemporaryFile
import shutil
from Archivos import lecturaArchivos as lec

class classPrestamo:
    
    def __init__(self,idprestamo, estudiante, objeto, fechaprestamo, fecharetorno):
        self.idprestamo= idprestamo
        self.estudiante = estudiante
        self.objeto = objeto
        self.fechaprestamo = fechaprestamo
        self.fecharetorno = fecharetorno
    
    def hacerPrestamo(self, estudiante, objeto, fechaprestamo,fecharetorno):
        arcp = archi(self.idprestamo, self.estudiante, self.objeto, self.fechaprestamo, self.fecharetorno)
        self.idprestamo = arcp.obtenerIncremental()
        self.escribirPrestamo(self.idprestamo, estudiante,objeto,fechaprestamo,fecharetorno)
        print("El prestamo ha sido registrado!")

    def hacerRetorno(self, idprestamo, fecharetorno):
        matricula = None
        idprestamo = int(input("Ingresa el id del prestamo: "))
        self.escribirRetorno(idprestamo,fecharetorno)

    def verPrestamos(self):
        for prestamo in setsPrestamo: 
            pre = {
                "idprestamo":prestamo.idprestamo,
                "estudiante":prestamo.estudiante,
                "objeto":prestamo.objeto,
                "fechaprestamo":prestamo.fechaprestamo,
                "fecharetorno":prestamo.fecharetorno,
                }
            print(pre) 

    def validaEstudiante(self,matricula):
        debe = False
        filename = 'estudiantes.csv'
        clave = None
        with open(filename,'r') as file:
            csv_reader = csv.DictReader(file, fieldnames = ['matricula','nombre','grupo','adeudo'])
            for row in csv_reader:
                if row['matricula']  == str(matricula) :
                    debe = row['adeudo']
        return debe
    
    def escribirPrestamo(self,idprestamo, estudiante, objeto, fechaprestamo, fecharetorno):
        with open('prestamos.csv', 'a', newline='\n') as file:
                csv_escritor = csv.DictWriter(
                    file, fieldnames=['idprestamo', 'estudiante', 'objeto', 'fechaprestamo','fecharetorno'])

                if file.tell() == 0:
                    csv_escritor.writeheader()

                csv_escritor.writerow({'idprestamo': idprestamo,
                                   'estudiante': estudiante,
                                   'objeto': objeto,
                                   'fechaprestamo': fechaprestamo,
                                   'fecharetorno': fecharetorno
                                   })
    
    def escribirRetorno(self,idprestamo,fecharetorno):
        matricula = 0
        nombre = ""
        grupo = ""
        adeudo = None
        e = lec(matricula,nombre,grupo,adeudo)
        tempfile = NamedTemporaryFile(mode='w', delete = False,encoding='utf8', newline='')
        filename = 'prestamos.csv'
        clave = None
        with open(filename,'r') as file, tempfile:
            csv_reader = csv.DictReader(file, fieldnames = ['idprestamo', 'estudiante', 'objeto', 'fechaprestamo','fecharetorno'])
            writer = csv.DictWriter(tempfile, fieldnames = ['idprestamo', 'estudiante', 'objeto', 'fechaprestamo','fecharetorno'])
            
            for row in csv_reader:
                if row['idprestamo']  == str(idprestamo):
                    print('prestamo a actualizar->',row['idprestamo'])
                    row['fecharetorno'] = fecharetorno
                    clave = row['estudiante']
                row = {'idprestamo': row['idprestamo'], 'estudiante': row['estudiante'], 'objeto': row['objeto'], 'fechaprestamo': row['fechaprestamo'],'fecharetorno': row['fecharetorno']}
                writer.writerow(row)

        shutil.move(tempfile.name, filename)
        e.cambiarAdeudo(clave)