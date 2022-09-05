class Empleados:
    def __init__(self, codEmp, nomEmp,puesEmp ):
        self.codEmp = codEmp
        self.nomEmp = nomEmp
        self.puesEmp = puesEmp

    def getCodEmp(self):
        return self.codEmp

    def setCodEmp(self, codEmp):
        self.codEmp = codEmp

    def getNomEmp(self):
        return self.nomEmp

    def setNomEmp(self, nomEmp):
        self.nomEmp = nomEmp

    def getPuesEmp(self):
        return self.puesEmp

    def setNomProv(self, puesEmp):
        self.puesEmp = puesEmp
    
    def __repr__(self):
        return f"Codigo: {self.codEmp}, Nombre: {self.nomEmp}"
