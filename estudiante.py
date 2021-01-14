class estudiante:
    def __init__(self):
        self.nombre = {}
        self.grupo = {}
    
    def ingresarDatos(self):
        self.nombre = input("Ingresar nombre: ")
        self.grupo = input("Ingresar grupo: ")
    
    def verEstudiante(self):
        print("Nombre: ",self.nombre)
        print("Grupo: ",self.grupo)




