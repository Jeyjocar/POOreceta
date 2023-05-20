from ingrediente import Ingredientes
import os

class Receta:
    agregar_ingrediente=1
    consultar_ingrediente=2
    agregar_procedimiento=3
    consultar_procedimiento=4
    salir=0

    def __init__(self, nombreReceta=""):
        self._nombreReceta=nombreReceta
        self._ingredientes=[]
        self._procedimientos=[]

    def __str__(self):
        texto= f'***********{self.nombreReceta}*********** \n'
        texto+="Ingredientes: \n"
        for ingrediente in self.ingredientes:
            texto+=f'{ingrediente}\n'
        texto+="Procedimientos: \n"
        for i,procedimiento in enumerate(self.procedimientos):
            texto+=f"{i+1}.{procedimiento}\n"
        return texto

    @property
    def nombreReceta(self):
        return self._nombreReceta
    
    @nombreReceta.setter
    def nombreReceta(self,valor):
        self._nombreReceta=valor
    
    @nombreReceta.deleter
    def nombreReceta(self):
        del self._nombreReceta

    @property
    def ingredientes(self):
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self,valor):
        self._ingredientes=valor
    
    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes
    
    @property
    def procedimientos(self):
        return self._procedimientos
    
    @procedimientos.setter
    def procedimientos(self,valor):
        self._procedimientos=valor
    
    @procedimientos.deleter
    def procedimientos(self):
        del self._procedimientos

    def menu(self):
        ejecutar=True
        while ejecutar:
            os.system("cls") #para limpiar la pantalla
            print(f'''{self._nombreReceta} Su receta
            {self.agregar_ingrediente}) Agregar_ingredientes
            {self.consultar_ingrediente}) Consultar_ingredientes
            {self.agregar_procedimiento}) Agregar_procedimientos
            {self.consultar_procedimiento}) Consultar_procedimientos
            {self.salir}) Salir
            ''')
            opcion=int(input("Por favor, ingrese alguna de las opciones anteriores: "))
            if opcion==self.agregar_ingrediente:
                self.AgregarIngrediente()
            elif opcion==self.consultar_ingrediente:
                self.ConsultarIngrediente()
            elif opcion==self.agregar_procedimiento:
                self.AgregarProcedimiento()
            elif opcion==self.consultar_procedimiento:
                self.ConsultarProcedimiento()
            elif opcion==self.salir:
                ejecutar=False
            else:
                print("La opción ingresada no es correcta")
            input("Presiona Enter para seguir")


    def AgregarIngrediente(self):
        continuar=True
        while continuar:
            os.system("cls")
            print("Agregando ingredientes")
            nombre=input("¿Que ingrediente desea agregar?: ")
            cantidad=-1        
            while cantidad<=0:
                cantidad=input("ingrese la cantidad del ingrediente ")
                try: #prueba
                    cantidad=float(cantidad)
                except: #excepcion
                    cantidad=0
            unidadMedida=input("Ingrese unidad de medida: ")
            ingrediente=Ingredientes(nombre,cantidad, unidadMedida)
            self.ingredientes.append(ingrediente)
            agregaOtro=input("¿Desea agregar otro ingrediente?: (S/N) ")
            if agregaOtro!="S" and agregaOtro !="s":
                continuar=False


    def ConsultarIngrediente(self):
        os.system("cls")
        print("Los ingredientes son: ")
        if len(self.ingredientes)==0:
            print("Oye no hay ingredientes registrados!!! ")
        else:
            for ingrediente in self.ingredientes:
                print(f'{ingrediente}')

    def AgregarProcedimiento(self):
        continuar=True
        while continuar:
            os.system("cls")
            print("Agregar Procedimiento a la receta: ")
            nombre=input("¿cual es tu procedimiento?: ")
            self.procedimientos.append(nombre)
            agregarOtro=input("¿Deseas agregar otro procedimiento?: (S/N) ")
            if agregarOtro!="S" and agregarOtro!="s":
                continuar=False

    def ConsultarProcedimiento(self):
        os.system("cls")
        print("Mostrando los procedimientos" )
        if len(self.procedimientos)==0:
            print("No existe ningún procedimiento cargado" )
        else:
            for i,procedimiento in enumerate(self.procedimientos):
                print(f'{i+1}.{procedimiento}')
