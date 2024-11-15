class Control:
    def __init__(self):
        self._tv = None
    
    def enlazar(self, tv):
        tv.setControl(self)
        self._tv = tv
    
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, nuevoCanal):
        self._tv.setCanal(nuevoCanal)

    def setVolumen(self, nuevoVolumen):
        self._tv.setVolumen(nuevoVolumen)
    
    def getTv(self):
        return self._tv
    def setTv(self, nuevoTv):
        self._tv = nuevoTv
