from envio import Envio


class Sobre(Envio):
    def calculaCosto(self):
        print("calculaCosto desde sobre")

    def __str__(self):
        return "Sobre"
