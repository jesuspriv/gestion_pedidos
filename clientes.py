class ListaClientesFrecuentes:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)
            print(f"Cliente {cliente} agregado a la lista de clientes frecuentes.")
        else:
            print(f"Cliente {cliente} ya está en la lista de clientes frecuentes.")

    def mostrar_clientes(self):
        return self.clientes
