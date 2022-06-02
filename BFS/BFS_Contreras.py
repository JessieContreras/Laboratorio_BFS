#Primero en Entrar, Primero en Salir
from queue import Queue

#Crea una función llamada Grafo.
class grafo:
    
    def __init__(self, numerosNodos, dirigrafo=True): #inicializamos los metodo.
        self.m_numero_de_nodos = numerosNodos #ingreso de los atributos del nodo.
        self.m_nodos = range(self.m_numero_de_nodos) #ingreso del rango del nodo
       