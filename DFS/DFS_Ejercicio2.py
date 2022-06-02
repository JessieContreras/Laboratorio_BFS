#Primero en Entrar, Primero en Salir
from queue import Queue

#Crea una función llamada Grafo.
class grafo:
    
    def __init__(self, numerosNodos, dirigrafo=True): #inicializamos los metodo.
        self.m_numero_de_nodos = numerosNodos #ingreso de los atributos del nodo.
        self.m_nodos = range(self.m_numero_de_nodos) #ingreso del rango del nodo
       
        self.m_dirigrafo= dirigrafo #Grafo dirigido 
       
        self.m_adj_lista = {nodo: set() for nodo in self.m_nodos} #Se crea una lista adyacente mediante un diccionario.
   
    def add_grafo(self, nodo1, nodo2, peso=1): #Se inicializa los nodos, diriguiendolos al borde del grafo
        self.m_adj_lista[nodo1].add((nodo2, peso))#hace funcion al nodo no dirigido.
       
        if not self.m_dirigrafo:
            self.m_adj_lista[nodo2].add((nodo1, peso)) # tomamo el nodo 2 y el nodo 1 se ubica al borde
    
    def print_adj_lista(self):# Representacion grafica def 
        #Numeros de nodos claves
        for llave in self.m_adj_lista.keys(): 
            print("nodo", llave, ": ", self.m_adj_lista[llave])# Imprime los nodos con la llave
 