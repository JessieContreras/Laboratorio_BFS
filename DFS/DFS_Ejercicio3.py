
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
 
 #Agregamos el nodo de inicio al comienzo de nuestra ruta transversal y lo marcamos como 
 # visitado al agregarlo a un conjunto de nodos visitados
    def dfs(self, inicio, objetivo, ruta = [], visita = set()):
        ruta.append(inicio)
        #Agregamos el nodo de inicio al comienzo de nuestra ruta
        visita.add(inicio)
        if inicio == objetivo: #y nos preguntamos si el inicio es igual al objetivo
            return ruta# y nos devuele la ruta
        #llamamos a la función recursivamente para cada uno de ellos
        for (neighbour, peso) in self.m_adj_lista[inicio]:
            if neighbour not in visita:
                resultado = self.dfs(neighbour, objetivo, ruta, visita)
                if resultado is not None:
                    #guardamos una referencia al resultado
                    return resultado
 #hemos encontrado nuestro nodo de destino y 
                # devolvemos la ruta transversal como resultado.
        ruta.pop()
        return None

if __name__ == "__main__":
    
    #Esto creará la instancia del Grafo de gráfico no dirigido que representa con un N nodos
    grafo = grafo(9, dirigrafo = False) #Ingresamos el numero de datos a imprimir
    print("Busqueda por Profundidad")
    
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
    
     #Proceso de Agregar bordes al gráfico con peso predeterminado = 1
    """Esta la congugacion de cada uno de los valores dependeiendi el nodo al que se encuentra"""
    grafo.add_grafo(dato1, dato2, dato1)
    grafo.add_grafo(dato1, dato3, dato1)  
    grafo.add_grafo(dato2,dato4,dato2)
    grafo.add_grafo(dato2,dato5,dato2)
    grafo.add_grafo(dato3,dato6,dato3)
    grafo.add_grafo(dato3,dato7,dato3)
    grafo.add_grafo(dato3,dato8,dato3)
    grafo.add_grafo(dato5,dato6,dato5)
    
     # Imprime las listas adyacentes  con su respectivo nodo y peso del borde.
    grafo.print_adj_lista()
    
    traversal_path = []
    traversal_path = grafo.dfs(0, 8)
    print(f" El camino transversal del nodo 1 al 8 nodo es {dato1, dato2, dato5, dato6, dato3, dato8}")