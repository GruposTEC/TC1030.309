from envio import Envio
from sobre import Sobre
from paquete import Paquete


class Fonda:
    def calculaCosto(self):
        print("calcula costo dentro de la fonda")


class Paqueteria:
    def maneja_paquete(self, cualquierEnvio):
        cualquierEnvio.calculaCosto()


env1 = Envio()
paq1 = Paquete()
sob1 = Sobre()

fondamexicana = Fonda()

dhl = Paqueteria()
dhl.maneja_paquete(env1)
dhl.maneja_paquete(paq1)
dhl.maneja_paquete(sob1)

print(isinstance(env1, Envio))
print(isinstance(paq1, Envio))
print(isinstance(sob1, Envio))
print(isinstance(fondamexicana, Envio))
dhl.maneja_paquete(fondamexicana)
