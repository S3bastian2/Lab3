from Agenda import Agenda
 
A = Agenda.importar("Agenda.txt")
r = A.getRegistro()
for i in range(len(r)):
    print(r[i])

A.eliminar(5)
A.toFile