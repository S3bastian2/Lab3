import os
from Usuario import *
class Agenda():
    def __init__(self, registro = None, no_reg = 0):
        self.__registro = registro if registro is not None else []
        self.__no_reg = no_reg
        
    def buscar(self, id_buscado): #Método buscar, recibe como parametros el id del usuario
        for ids in range(self.__no_reg):
            if isinstance(self.__registro[ids], Usuario):
                if self.__registro[ids].getId() == id_buscado: #Comparamos cada id de los objetos con el id presentado
                    return ids #Si la comparación es verdadera entonces retornamos el indice de dicho objeto
        else: #En caso de no haberse encontrado comparación similar
            return -1 #Retornamos menos uno

    def agregar(self, u):
        if self.buscar(u.getId()) != -1: #Tomamos el id del usuario y se lo pasamos al método buscar, si este obtiene un valor diferente de menos 1 retornara False
            return False #Retorna False pues el objeto ya pertenece al arreglo
        else:
            self.__registro.append(u) #Si el valor retornado fue menos uno, entonces se agrega el nuevo objeto al arreglo
            self.__no_reg += 1 #Aumenta el tamaño del arreglo
            return True #Retorna True porque el nuevo objeto fue agregado con exito
    
    def eliminar(self, id): #Método que elimina objetos
        if self.buscar(id) == -1: #Us0ando el método buscar se fija si el objeto esta en el arreglo, si no esta retorna Falso
            return False #Retorna Falso porque no se encontraba el objeto
        else: #En caso de que el objeto este
            indice_eliminado = self.buscar(id)
            for i in range(indice_eliminado, self.__no_reg-2): #Se empieza a iterar desde el indice del objeto eliminado
                self.__registro[i] = self.__registro[i+1] #Se mueven los objetos hacia la ¿izquierda?
            self.__registro[self.__no_reg-1] = None #El ultimo valor del arreglo ya no esta pues todo fue ocupado por los demas valores
            self.__no_reg -= 1 #Disminuimos el tamaño del arreglo
            return True #Devolvemos Verdadero tras haberse completado todo el proceso
        
    def getRegistro(self):
        return self.__registro
        
    def toFile(self):
        if os.path.exists("/Agenda.txt"):
            archivo = open("Agenda2.txt", "w")
            for objeto in self.__registro:
                if objeto != None:
                    archivo.write(f"{Usuario.getNombre(objeto)}, {Usuario.getId(objeto)}, {Usuario.getFechaNacimiento(objeto)}, {Usuario.getCiudadNacimiento(objeto)}, {Usuario.getTelefono(objeto)}, {Usuario.getEmail(objeto)}, {Usuario.getDir(objeto)} \n")
            archivo.close()
            
        else:    
            archivo = open("Agenda.txt", "w")
            for objeto in self.__registro:
                if objeto != None:
                    archivo.write(f"{Usuario.getNombre(objeto)}, {Usuario.getId(objeto)}, {Usuario.getFechaNacimiento(objeto)}, {Usuario.getCiudadNacimiento(objeto)}, {Usuario.getTelefono(objeto)}, {Usuario.getEmail(objeto)}, {Usuario.getDir(objeto)} \n")
            archivo.close()
    
    def importar(self):
        with open("Agenda.txt", "r") as archivo:
            Usus = []
            x = 0
            for i in archivo:
                listaUsuarios = i.split(",")
                usuario = Usuario(str(listaUsuarios[0]),int(listaUsuarios[1]),str(listaUsuarios[3]),int(listaUsuarios[4]),str(listaUsuarios[5]))
            
                x = listaUsuarios[2].split()
                dd = x[0]
                mm = x[1]
                aa = x[2]
                usuario.setFechaNacimiento(Fecha(dd,mm,aa))
                
                y = listaUsuarios[6].split()
                calle = y[0]
                nomenclatura = y[1] 
                barrio = y[2]
                ciudad = y[3]
                edificio = y[4]
                apto = y[5]
                usuario.setDir(Direccion(calle, nomenclatura, barrio, ciudad, edificio, apto))
                
                Usus.append(usuario)
        return Agenda(Usus, len(Usus))