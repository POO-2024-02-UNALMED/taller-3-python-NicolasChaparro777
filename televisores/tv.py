class TV:
    __numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV.__numTV += 1
    
    def getCanal(self):
        return self._canal
    def setCanal(self, nuevoCanal):
        if self._estado == True:
            if 1<= nuevoCanal <= 120:
                self._canal = nuevoCanal

    def getVolumen(self):
        return self._volumen
    def setVolumen(self, nuevoVolumen):
        if self._estado == True:
            if 0 <= nuevoVolumen <= 7:
                self._volumen = nuevoVolumen
    
    def getMarca(self):
        return self._marca
    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca
    
    def getPrecio(self):
        return self._precio
    def setPrecio(self, nuevoPrecio):
        self._precio = nuevoPrecio
    
    def getControl(self):
        return self._control
    def setControl(self, nuevoControl):
        self._control = nuevoControl

    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado == True:
            if self._canal < 120:
                self._canal += 1
    def canalDown(self):
        if self._estado == True:
            if self._canal > 1:
                self._canal -= 1
    
    def volumenUp(self):
        if self._estado == True:
            if self._volumen < 7:
                self._volumen += 1
    def volumenDown(self):
        if self._estado == True:
            if self._volumen > 0:
                self._volumen -= 1
    
    def setNumTV(self, nuevoNum):
        TV.__numTV = nuevoNum
