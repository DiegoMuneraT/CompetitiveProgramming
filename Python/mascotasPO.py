class Mascota(object):
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def darNombre(self):
        return self.nombre

    def darEspecie(self):
        return self.especie

    def __str__(self):
        return "Es un "+self.nombre, self.especie