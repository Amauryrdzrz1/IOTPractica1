import csv
from archivoObjetos import archivoObjetos as o
class classObjeto:

    def __init__(self, claveObjeto, nombre):
        self.claveObjeto = claveObjeto
        self.nombre = nombre

    def ingresarObjeto(self, nombre):
        obtenIncremental = o(self.claveObjeto,self.nombre)
        self.claveObjeto = obtenIncremental.obtenerIncremental()
        self.nombre = nombre
        self.escribirObjetos(self.claveObjeto,self.nombre)

    def buscarObjeto(self, claveObjeto):
        self.claveObjeto = int(input("ingresa la clave del objeto: "))
        buscar = o(self.claveObjeto,self.nombre)
        matr = buscar.buscarObjeto(self.claveObjeto)
        return matr;

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

    def escribirObjetos(self, claveObjeto, nombre):

        with open('objetos.csv', 'a', newline='\n') as file:
            csv_escritor = csv.DictWriter(file, fieldnames=['claveObjeto', 'nombre'])

            if file.tell() == 0:
                csv_escritor.writeheader()

            csv_escritor.writerow({'claveObjeto': claveObjeto,
                                   'nombre': nombre,
                                   })