from Clases.Usuario import Usuario
class Agenda():
    def __init__(self, registro = None, no_reg = 0):
        self.__registro = registro if registro is not None else []
        self.__no_reg = no_reg
        
    def buscar(id): #Método buscar, recibe como parametros el id del usuario
        id_buscado = id #Variable que almacena el id que queremos comparar
        for ids in range(Agenda.__no_reg): #Ciclo que recorre el arreglo hasta los objetos que hayamos decidido meter en el
            if Agenda.__registro[ids].id == id_buscado: #Comparamos cada id de los objetos con el id presentado
                return ids #Si la comparación es verdadera entonces retornamos el indice de dicho objeto
        else: #En caso de no haberse encontrado comparación similar
            return -1 #Retornamos menos uno

    def agregar(u):
        if Agenda.buscar(u.getId()) != -1: #Tomamos el id del usuario y se lo pasamos al método buscar, si este obtiene un valor diferente de menos 1 retornara False
            return False #Retorna False pues el objeto ya pertenece al arreglo
        else:
            Agenda.__registro.append(u) #Si el valor retornado fue menos uno, entonces se agrega el nuevo objeto al arreglo
            Agenda.__no_reg += 1 #Aumenta el tamaño del arreglo
            return True #Retorna True porque el nuevo objeto fue agregado con exito
    
    def eliminar(id): #Método que elimina objetos
        if Agenda.buscar(id) == -1: #Usando el método buscar se fija si el objeto esta en el arreglo, si no esta retorna Falso
            return False #Retorna Falso porque no se encontraba el objeto
        else: #En caso de que el objeto este
            indice_eliminado = Agenda.buscar(id)
            for i in range(indice_eliminado, Agenda.__no_reg-2): #Se empieza a iterar desde el indice del objeto eliminado
                Agenda.__registro[i] = Agenda.__registro[i+1] #Se mueven los objetos hacia la ¿izquierda?
            Agenda.__registro[Agenda.__no_reg-1] = None #El ultimo valor del arreglo ya no esta pues todo fue ocupado por los demas valores
            Agenda.__no_reg -= 1 #Disminuimos el tamaño del arreglo
            return True #Devolvemos Verdadero tras haberse completado todo el proceso
        
    def toFile(self, archivo):
        f = open(archivo, "w")
        for objeto in Agenda.__registro:
            if objeto != None:
                f.write(f"{Usuario.getNombre(), Usuario.getId(), Usuario.getFechaNacimiento(), Usuario.getCiudadNacimiento(), Usuario.getTelefono(), Usuario.getEmail(), Usuario.getDir()}")
        f.close()
    
    def importar():
        pass