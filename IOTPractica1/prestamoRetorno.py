arrayPrestamoRetorno = []
setsPrestamo = []
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
    