import csv
from archivoPrestamos import archivoPrestamos as archi
class classPrestamo:
    
    def __init__(self,idprestamo, estudiante, objeto, fechaprestamo, fecharetorno):
        self.idprestamo= idprestamo
        self.estudiante = estudiante
        self.objeto = objeto
        self.fechaprestamo = fechaprestamo
        self.fecharetorno = fecharetorno
    
    def hacerPrestamo(self, estudiante, objeto, fechaprestamo,fecharetorno):
        self.idprestamo = self.idprestamo + 1
        setsPrestamo.append(classPrestamo(self.idprestamo,estudiante,objeto,fechaprestamo,fecharetorno))
        print("El prestamo ha sido registrado!")

    def hacerRetorno(self, idprestamo, fecharetorno):
        idx = 0
        matricula = None
        idprestamo = int(input("Ingresa el id del prestamo: "))
        for prestamo in setsPrestamo: 
            if prestamo.idprestamo == idprestamo and prestamo.fecharetorno == None:
                prestamo.fecharetorno = fecharetorno
                pre = {
                    "idprestamo":prestamo.idprestamo,
                    "estudiante":prestamo.estudiante,
                    "objeto":prestamo.objeto,
                    "fechaprestamo":prestamo.fechaprestamo,
                    "fecharetorno":prestamo.fecharetorno,
                    }
                print(pre)
                setsPrestamo.pop(idx)
                setsPrestamo.append(classPrestamo(prestamo.idprestamo,prestamo.estudiante,prestamo.objeto,prestamo.fechaprestamo,prestamo.fecharetorno))
                matricula = prestamo.estudiante
            idx = idx + 1
        return matricula

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
        for prestamo in setsPrestamo: 
            if prestamo.estudiante == matricula and prestamo.fecharetorno == None:
                debe = True
                pre = {
                    "idprestamo":prestamo.idprestamo,
                    "estudiante":prestamo.estudiante,
                    "objeto":prestamo.objeto,
                    "fechaprestamo":prestamo.fechaprestamo,
                    "fecharetorno":prestamo.fecharetorno,
                    }
                print(pre)
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
    