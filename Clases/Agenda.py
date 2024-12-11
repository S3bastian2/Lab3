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
        
    def toFile(self, archivo):
        f = open(archivo, "w")
        for objeto in self.__registro:
            if objeto != None:
                f.write(f"{Usuario.getNombre()}, {Usuario.getId()}, {Usuario.getFechaNacimiento()}, {Usuario.getCiudadNacimiento()}, {Usuario.getTelefono()}, {Usuario.getEmail()}, {Usuario.getDir()}")
        f.close()
    
    def importar(self, archivo):
        with open("Agenda.txt", "r") as archivo:
            for i in archivo:
                listaUsuarios = i.split(",")
                usuario = Usuario(str(listaUsuarios[0]),int(listaUsuarios[1]),str(listaUsuarios[3]),int(listaUsuarios[4]),str(listaUsuarios[5])) 
                Usuario.setFechaNacimiento(listaUsuarios[2])
                Usuario.setDir(listaUsuarios[6])
                self.__registro.append(usuario)
                self.__no_reg += 1