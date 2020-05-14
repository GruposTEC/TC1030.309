class Persona():
    """Clase que especifica las caracteristicas de una Persona
         Es la base para realizar herencia
    """

    def __init__(self, nombre):
        self.nombre = nombre

    def hablo(self):
        return "Soy una persona y puedo hablar"

    def __str__(self):
        return f'Mi nombre es : {self.nombre}'


def main():
    javier = Persona("Javier")
    pedro = Persona("Pedro")
    print(javier)
    print(pedro)
    print(javier.hablo())


if __name__ == '__main__':
    main()
