from Fecha import Fecha
from Direccion import Direccion
from Agenda import Agenda
from Usuario import Usuario

u1 = Usuario("David", 1, "Valledupar", 3134697894, "david@recocha.edu.co")
f1 = Fecha(13, 11, 2006)
d1 = Direccion("Kra 92", "74B-08", "Robledo", "Medellín", None, None)

u1.setFechaNacimiento(f1)
u1.setDir(d1)

u2 = Usuario("Carlos", 2, "Bogotá", 3123456789, "carlos@ejemplo.com")
f2 = Fecha(25, 5, 1992)
d2 = Direccion("Av. Chile", "21A-12", "Teusaquillo", "Bogotá", None, None)

u2.setFechaNacimiento(f2)
u2.setDir(d2)

u3 = Usuario("Ana", 3, "Medellín", 3145678901, "ana@correo.com")
f3 = Fecha(7, 8, 1990)
d3 = Direccion("Calle 45", "23B-09", "Laureles", "Medellín", None, None)

u3.setFechaNacimiento(f3)
u3.setDir(d3)

u4 = Usuario("Luis", 4, "Cali", 3156789012, "luis@ejemplo.com")
f4 = Fecha(10, 12, 1985)
d4 = Direccion("Calle 75", "14A-11", "San Fernando", "Cali", None, None)

u4.setFechaNacimiento(f4)
u4.setDir(d4)

u5 = Usuario("Laura", 5, "Barranquilla", 3178901234, "laura@correo.com")
f5 = Fecha(15, 3, 1995)
d5 = Direccion("Carrera 50", "9B-03", "Centro", "Barranquilla", None, None)

u5.setFechaNacimiento(f5)
u5.setDir(d5)

A1 = Agenda([u1, u2, u3, u4, u5], 5)

print(A1.buscar(3))