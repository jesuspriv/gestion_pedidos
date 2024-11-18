class Pedido:
    def __init__(self, id, cliente, categoria):
        self.id = id
        self.cliente = cliente
        self.categoria = categoria

# Cola Circular para pedidos en espera
class ColaCircular:
    def __init__(self, max_size=10):
        self.cola = [None] * max_size
        self.max_size = max_size
        self.front = 0
        self.rear = -1
        self.size = 0

    def esta_llena(self):
        return self.size == self.max_size

    def esta_vacia(self):
        return self.size == 0

    def agregar_pedido(self, pedido):
        if not self.esta_llena():
            self.rear = (self.rear + 1) % self.max_size
            self.cola[self.rear] = pedido
            self.size += 1
        else:
            print("La cola de pedidos está llena.")

    def eliminar_pedido(self):
        if not self.esta_vacia():
            pedido = self.cola[self.front]
            self.cola[self.front] = None
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return pedido
        else:
            print("La cola de pedidos está vacía.")
        return None

# Pila para pedidos cancelados
class PilaPedidosCancelados:
    def __init__(self):
        self.pila = []

    def cancelar_pedido(self, pedido):
        self.pila.append(pedido)

    def restaurar_pedido(self):
        if self.pila:
            return self.pila.pop()
        else:
            print("No hay pedidos para restaurar.")
        return None
