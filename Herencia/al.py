from persona import Persona


class Alumno(Persona):

    num_registro: 1300000

    def __init__(self, nom, carr, univ):
        super().__init__(nom)
        self.matr = Alumno.num_registro
        self.carrera = carr
        self.universidad = univ
        Alumno.num_registro = Alumno.num_registro + 1


al1 = Alumno("Pedro Perez")
print(al1)
