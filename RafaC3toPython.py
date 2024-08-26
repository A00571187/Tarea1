import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import pandas as pd

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Aplicación")
root.geometry("500x400")

# Configuración del estilo de la interfaz
style = ttk.Style()
style.theme_use("clam")  # Cambiar a un estilo moderno

def validar_entrada():
    if entry1.get() == "" or entry2.get() == "" or not entry1.get().isdigit() or not entry2.get().isdigit() or int(entry1.get()) <= 0 or int(entry2.get()) <= 0:
        messagebox.showwarning("Advertencia", "Los números deben ser mayores a cero y no vacíos.")
        return False
    return True

def llenar_grid(lista):
    # Limpiar el Treeview antes de agregar datos nuevos
    for item in treeview.get_children():
        treeview.delete(item)

    # Llenar filas
    for i, valor in enumerate(lista):
        treeview.insert("", "end", values=(i + 1, valor))

def ejecutar():
    if not validar_entrada():
        return
    
    total_valores = int(entry1.get())
    
    # Generar una lista de valores aleatorios
    lista_valores = [random.randint(1, 100) for _ in range(total_valores)]
    
    # Llenar el grid con la lista generada
    llenar_grid(lista_valores)

def borrar_datos():
    # Limpiar todos los elementos del Treeview
    for item in treeview.get_children():
        treeview.delete(item)

def exportar_csv():
    # Obtener los datos del Treeview
    filas = [treeview.item(item)["values"] for item in treeview.get_children()]
    df = pd.DataFrame(filas, columns=["Id", "Valor"])

    # Guardar archivo CSV
    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if archivo:
        df.to_csv(archivo, index=False)
        messagebox.showinfo("Éxito", "Datos exportados exitosamente a CSV.")

# Crear los widgets en Frames para mejor organización
frame_inputs = ttk.Frame(root, padding="10")
frame_inputs.grid(row=0, column=0, sticky="ew")

label1 = ttk.Label(frame_inputs, text="Parámetro 1")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = ttk.Entry(frame_inputs)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = ttk.Label(frame_inputs, text="Parámetro 2")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = ttk.Entry(frame_inputs)
entry2.grid(row=1, column=1, padx=5, pady=5)

button_ejecutar = ttk.Button(frame_inputs, text="Ejecutar", command=ejecutar)
button_ejecutar.grid(row=2, column=0, columnspan=2, pady=10)

# Crear el Treeview (similar a DataGridView)
columns = ("Id", "Valor")
treeview = ttk.Treeview(root, columns=columns, show="headings")
treeview.heading("Id", text="Id")
treeview.heading("Valor", text="Valor")
treeview.column("Id", width=100)
treeview.column("Valor", width=100)
treeview.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Crear el botón de exportar
button_exportar = ttk.Button(root, text="Descarga", command=exportar_csv)
button_exportar.grid(row=2, column=0, pady=5)

# Crear el botón de borrar
button_borrar = ttk.Button(root, text="Borrar", command=borrar_datos)
button_borrar.grid(row=3, column=0, pady=5)

# Configurar expansión del Treeview para ajustarse a la ventana
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Iniciar el bucle principal de la aplicación
root.mainloop()
