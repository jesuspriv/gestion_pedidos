class NodoCategoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None

class ArbolCategorias:
    def __init__(self):
        self.raiz = None

    def agregar_categoria(self, nombre):
        if self.raiz is None:
            self.raiz = NodoCategoria(nombre)
        else:
            self._insertar(self.raiz, nombre)

    def _insertar(self, nodo, nombre):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = NodoCategoria(nombre)
            else:
                self._insertar(nodo.izquierda, nombre)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoCategoria(nombre)
            else:
                self._insertar(nodo.derecha, nombre)

    def mostrar_categorias(self):
        def recorrido_inorden(nodo):
            if nodo:
                recorrido_inorden(nodo.izquierda)
                print(nodo.nombre)
                recorrido_inorden(nodo.derecha)
        recorrido_inorden(self.raiz)
