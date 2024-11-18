import tkinter as tk
from pedido import Pedido, ColaCircular, PilaPedidosCancelados
from clientes import ListaClientesFrecuentes
from categoria import ArbolCategorias

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pedidos - Restaurante")

        # Inicialización de estructuras
        self.cola_pedidos = ColaCircular()
        self.pila_cancelados = PilaPedidosCancelados()
        self.clientes_frecuentes = ListaClientesFrecuentes()
        self.arbol_categorias = ArbolCategorias()

        # Frame principal
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Formulario para añadir pedidos
        tk.Label(self.frame, text="ID Pedido").grid(row=0, column=0)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Nombre Cliente").grid(row=1, column=0)
        self.cliente_entry = tk.Entry(self.frame)
        self.cliente_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Pedido").grid(row=2, column=0)
        self.categoria_entry = tk.Entry(self.frame)
        self.categoria_entry.grid(row=2, column=1)

        tk.Button(self.frame, text="Añadir Pedido", command=self.anadir_pedido).grid(row=3, column=0, columnspan=2, pady=5)

        # Botones de funcionalidad
        tk.Button(self.frame, text="Cancelar Pedido", command=self.cancelar_pedido).grid(row=4, column=0, columnspan=2)
        tk.Button(self.frame, text="Restaurar Pedido", command=self.restaurar_pedido).grid(row=5, column=0, columnspan=2)
        
        # Botones para mostrar listas
        tk.Button(self.frame, text="Mostrar Pedidos en Espera", command=self.mostrar_pedidos).grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(self.frame, text="Mostrar Clientes Frecuentes", command=self.mostrar_clientes_frecuentes).grid(row=7, column=0, columnspan=2)

        # Área de visualización de resultados
        self.resultado_text = tk.Text(self.frame, height=10, width=50)
        self.resultado_text.grid(row=8, column=0, columnspan=2, pady=10)

        # Formulario para añadir clientes frecuentes
        tk.Label(self.frame, text="Nombre Cliente Frecuente").grid(row=9, column=0)
        self.cliente_frecuente_entry = tk.Entry(self.frame)
        self.cliente_frecuente_entry.grid(row=9, column=1)
        tk.Button(self.frame, text="Agregar Cliente Frecuente", command=self.agregar_cliente_frecuente).grid(row=10, column=0, columnspan=2, pady=5)

    def anadir_pedido(self):
        # Recuperar datos del formulario
        id_pedido = self.id_entry.get()
        cliente = self.cliente_entry.get()
        categoria = self.categoria_entry.get()
        
        # Validar datos
        if id_pedido and cliente and categoria:
            pedido = Pedido(id=id_pedido, cliente=cliente, categoria=categoria)
            self.cola_pedidos.agregar_pedido(pedido)
            self.resultado_text.insert(tk.END, f"Pedido {id_pedido} añadido a la cola.\n")
            
            # Agregar categoría al árbol si no existe
            self.arbol_categorias.agregar_categoria(categoria)
        else:
            self.resultado_text.insert(tk.END, "Por favor, rellene todos los campos.\n")

    def cancelar_pedido(self):
        pedido = self.cola_pedidos.eliminar_pedido()
        if pedido:
            self.pila_cancelados.cancelar_pedido(pedido)
            self.resultado_text.insert(tk.END, f"Pedido {pedido.id} cancelado y añadido a la pila de cancelaciones.\n")
        else:
            self.resultado_text.insert(tk.END, "No hay pedidos en espera para cancelar.\n")

    def restaurar_pedido(self):
        pedido = self.pila_cancelados.restaurar_pedido()
        if pedido:
            self.cola_pedidos.agregar_pedido(pedido)
            self.resultado_text.insert(tk.END, f"Pedido {pedido.id} restaurado a la cola de pedidos.\n")
        else:
            self.resultado_text.insert(tk.END, "No hay pedidos para restaurar.\n")

    def mostrar_pedidos(self):
        self.resultado_text.delete(1.0, tk.END)  # Limpiar área de texto
        if self.cola_pedidos.esta_vacia():
            self.resultado_text.insert(tk.END, "No hay pedidos en espera.\n")
        else:
            self.resultado_text.insert(tk.END, "Pedidos en espera:\n")
            index = self.cola_pedidos.front
            for _ in range(self.cola_pedidos.size):
                pedido = self.cola_pedidos.cola[index]
                self.resultado_text.insert(tk.END, f"ID: {pedido.id}, Cliente: {pedido.cliente}, Categoría: {pedido.categoria}\n")
                index = (index + 1) % self.cola_pedidos.max_size

    def agregar_cliente_frecuente(self):
        cliente = self.cliente_frecuente_entry.get()
        if cliente:
            self.clientes_frecuentes.agregar_cliente(cliente)
            self.resultado_text.insert(tk.END, f"Cliente {cliente} añadido a la lista de clientes frecuentes.\n")
        else:
            self.resultado_text.insert(tk.END, "Por favor, ingrese el nombre del cliente.\n")

    def mostrar_clientes_frecuentes(self):
        self.resultado_text.delete(1.0, tk.END)
        clientes = self.clientes_frecuentes.mostrar_clientes()
        if clientes:
            self.resultado_text.insert(tk.END, "Clientes Frecuentes:\n")
            for cliente in clientes:
                self.resultado_text.insert(tk.END, f"- {cliente}\n")
        else:
            self.resultado_text.insert(tk.END, "No hay clientes frecuentes registrados.\n")

root = tk.Tk()
app = App(root)
root.mainloop()
