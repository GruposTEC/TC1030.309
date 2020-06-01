import os
import sys

if os.name == 'nt':
    direc = sys.path[0] + "\\"
else:
    direc = sys.path[0] + "/"

mal = direc + "prueba_1.txt"
ok = direc + "prueba.txt"


def metodo():
    raise ZeroDivisionError("algo paso")


try:
    f = open(mal)
    # metodo()
    #var = novar
except MemoryError as e:
    print("error de memoria")
    print(e)
except NameError:
    print("variable no reconocida")
except Exception as e:
    print(isinstance(e, ZeroDivisionError))
    print(isinstance(e, NameError))
    print("caida en la red")
else:
    print("No hubo excpeciones")
finally:
    print("siempre corro yo")
