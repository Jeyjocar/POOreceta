class Ingredientes():
    def __init__(self, nombre="" ,cantidad=None, unidadMedida=""):
        self._nombre=nombre
        self._cantidad=cantidad
        self._unidadMedida=unidadMedida

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,valor):
        self._nombre=valor

    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self,valor):
        self._cantidad=valor
    @cantidad.deleter
    def cantidad(self):
        del self._cantidad

    @property
    def unidadMedida(self):
        return self._unidadMedida

    @unidadMedida.setter
    def unidadMedida(self,valor):
        self._unidadMedida=valor

    @unidadMedida.deleter
    def unidadMedida(self):
        del self._unidadMedida

    def __str__(self):
        return f''' Receta {self._nombre}, {self._cantidad}, {self._unidadMedida}'''




