setsObjeto = []
class classObjeto:

    def __init__(self, claveObjeto, nombre):
        self.claveObjeto = claveObjeto
        self.nombre = nombre

    def ingresarObjeto(self, nombre):
        self.nombre = input("Ingresar Objeto: ")
        self.claveObjeto = self.claveObjeto + 1
        setsObjeto.append(classObjeto(self.claveObjeto,self.nombre))
        print("El objeto ha sido registrado!")
    
    def verObjeto(self):
        for objeto in setsObjeto: 
            obj = {
                "claveObjeto":objeto.claveObjeto,
                "Nombre":objeto.nombre,
                }
            print(obj) 

    def buscarObjeto(self, claveObjeto):
        self.claveObjeto = int(input("ingresa la clave del objeto: "))
        for objeto in setsObjeto: 
            if objeto.claveObjeto == self.claveObjeto:
                obj = {
                    "claveObjeto":objeto.claveObjeto,
                    "Nombre":objeto.nombre,
                    }
                print(obj) 
                return objeto.claveObjeto

    def eliminarObjeto(self, claveObjeto):
        self.claveObjeto = int(input("ingresa la clave del objeto a eliminar: "))
        idx = 0
        for objeto in setsObjeto: 
            if objeto.claveObjeto == self.claveObjeto:
                obj = {
                    "claveObjeto":objeto.claveObjeto,
                    "Nombre":objeto.nombre,
                    }
                print("El objeto ha sido removido: ")
                print(obj) 
                setsObjeto.pop(idx)
            idx += 1