class Cliente:
    def __init__(self, NitCl, nomCl):
        self.NitCl = NitCl
        self.nomCl = nomCl

    def getNitCl(self):
        return self.NitCl

    def setNitCl(self, NitCl):
        self.NitCl = NitCl

    def getNomCl(self):
        return self.nomCl

    def setNomCl(self, nomCl):
        self.nomCl = nomCl

    def __repr__(self):
        return f"NIT: {self.NitCl}, Nombre: {self.nomCl}"
