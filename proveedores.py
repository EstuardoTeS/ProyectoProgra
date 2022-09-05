class Proveedor:
    def __init__(self, codProv, nomProv):
        self.codProv = codProv
        self.nomProv = nomProv

    def getCodProv(self):
        return self.codProv

    def setCodProv(self, codProv):
        self.codProv = codProv

    def getNomProv(self):
        return self.nomProv

    def setNomProv(self, nomProv):
        self.nomProv = nomProv

    def __repr__(self):
        return f"Codigo: {self.codProv}, Nombre: {self.nomProv}"
