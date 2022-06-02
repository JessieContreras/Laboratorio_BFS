#Primero en Entrar, Primero en Salir
from queue import Queue
 
#Crea una función llamada Grafo.
class grafo:
   
    def __init__(self, numerosNodos, dirigrafo=True): #inicializamos los metodo.
        self.m_numero_de_nodos = numerosNodos #ingreso de los atributos del nodo.
        self.m_nodos = range(self.m_numero_de_nodos) #ingreso del rango del nodo
       
        self.m_dirigrafo= dirigrafo #Grafo dirigido
       
        self.m_adj_lista = {nodo: set() for nodo in self.m_nodos} #Se crea una lista adyacente mediante un diccionario.
   
    def add_edgrafo(self, nodo1, nodo2, peso=1): #Se inicializa los nodos, diriguiendolos al borde del grafo
        self.m_adj_lista[nodo1].add((nodo2, peso))#hace funcion al nodo no dirigido.
        if not self.m_dirigrafo:
            self.m_adj_lista[nodo2].add((nodo1, peso)) # tomamo el nodo 2 y el nodo 1 se ubica al borde
   
    def print_adj_lista(self):# Representacion grafica def
        #Numeros de nodos claves
        for llave in self.m_adj_lista.keys():
            print("nodo", llave, ": ", self.m_adj_lista[llave])# Imprime los nodos con la llave
 
    def bfs_traversal(self, iniciar_nodo): #funcion para imprimir los recorridos
        visita = set() #Conjunto de nodos visitados
        queue = Queue() #conjunto de colas
 
        queue.put(iniciar_nodo) #añadir a la cola, la lista visitada
        visita.add(iniciar_nodo)
 
        while not queue.empty(): #Cuando existen colas vacias.
           
            actual_nodo = queue.get()  # sacar de la cola los vértices.
            print(actual_nodo, end = " ") #Imprime el estado actual de los nodos inicial y final
            for (nodo_siguiente, peso) in self.m_adj_lista[actual_nodo]:
                if nodo_siguiente not in visita: #no ha sido visitado el nodo
                    queue.put(nodo_siguiente)#añade dentro de la cola
                    visita.add(nodo_siguiente) #agrega el dato
                    
if __name__ == "__main__": #ejecuta el codigo que son importante en el módulo
   
    grafo = grafo(10, dirigrafo=True) #Ingresamos el numero de datos a imprimir
    print("Busqueda por Anchura")
    #Ingreso de los datos
    """creamos una variables por cad auno de los datos que vamos a ingresar en este caso es de 8"""
   
    dato1=int(input("Ingrese un dato1: "))
    dato2=int(input("Ingrese un dato2: "))
    dato3=int(input("Ingrese un dato3: "))
    dato4=int(input("Ingrese un dato4: "))
    dato5=int(input("Ingrese un dato5: "))
    dato6=int(input("Ingrese un dato6: "))
    dato7=int(input("Ingrese un dato7: "))
    dato8=int(input("Ingrese un dato8: "))
    dato9=int(input("Ingrese un dato9: "))
    dato10=int(input("Ingrese un dato10: "))
      #Proceso de Agregar a lo bordes al gráfico con peso predeterminado = 1
    """Esta la conjugacion de cada uno de los valores dependiendo el nodo al que se encuentra"""
    grafo.add_edgrafo(dato1, dato8, dato1)
    grafo.add_edgrafo(dato1, dato5, dato1)  
    grafo.add_edgrafo(dato1, dato2, dato1)
    grafo.add_edgrafo(dato8,dato6,dato8)
    grafo.add_edgrafo(dato8,dato4,dato8)
    grafo.add_edgrafo(dato8,dato3,dato8)
    grafo.add_edgrafo(dato2,dato9,dato2)
    grafo.add_edgrafo(dato6,dato10,dato6)
    grafo.add_edgrafo(dato6,dato10,dato6)
 
    # Imprime las listas adyacentes  con su respectivo nodo y peso del borde.
    grafo.print_adj_lista()
    #Imprime el recorrido de la anchura que tiene el nodo.
    print ("A continuación se muestra el primer recorrido en anchura"
                    " (a partir del vértice 0)")
    #Indica el número de búsqueda de anchura.
    grafo.bfs_traversal(0)
    #Imprime los nodos en la cola por el lado mas cercano
    print(dato1, dato8, dato2, dato6, dato4, dato3, dato9, dato10, dato7)
 