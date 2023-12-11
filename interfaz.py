import tkinter as tk
from tkinter.font import Font
from tkinter import ttk, filedialog
import json
import os
from _source.pf_functions import pf_Object
from _source.pdf_functions import pdf_Object

# iniciamos 
pf_object = pf_Object()
pdf_object = pdf_Object()
# configuración inicial
# Lee el contenido del archivo JSON
ruta_completa = os.path.join(os.path.dirname(__file__), "data.json")
with open(ruta_completa, 'r') as archivo_json:
    datos_usuario = json.load(archivo_json)
archivo_pdf_full_name = None
app = None
tomar_archivo_save = False

def editar_output(text):
    salida.config(state="normal")  # Habilitar la edición
    salida.insert(tk.END, f"{text}\n\n")
    salida.config(state="disabled")  # Deshabilitar la edición

def seleccionar_archivo():
    # Utilizar el diálogo de selección de archivos
    archivo_pdf_full_name = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Carpeta", "*.pdf")])
    if archivo_pdf_full_name:
        # Mostrar la ruta del archivo seleccionado en la salida principal
        name_pdf = pdf_object.open_pdf(archivo_pdf_full_name)
        etiqueta_pdf.configure(text=f"Archivo PDF: {name_pdf}", foreground="green", font=("Arial", 12, "bold"))
        editar_output(f"Archivo seleccionado: {archivo_pdf_full_name}")
    else:
        editar_output("No hay archivo PDF seleccionado")

def seleccionar_carpeta():
    # Utilizar el diálogo de selección de archivos
    carpeta_seleccionada = filedialog.askdirectory(title="Seleccionar carpeta")
    # Hacer algo con la carpeta seleccionada, por ejemplo, imprimir la ruta
    try:
        python_dir = pf_object.open_folder(carpeta_seleccionada)
        editar_output(f"Conexión exitosa: {carpeta_seleccionada}")
        etiqueta_conexion.configure(text=f"Conexión DigSilent: {python_dir}", foreground="green", font=("Arial", 12, "bold"))
        # Modifica el valor que deseas cambiar
        datos_usuario["ruta_pf"] = carpeta_seleccionada
        # Guarda los cambios en el archivo JSON
        with open(ruta_completa, 'w') as archivo_json:
            json.dump(datos_usuario, archivo_json, indent=4)
    # ... some calculations ...
    except:
        editar_output(f"Error conexión PF: {carpeta_seleccionada}")   
def seleccionar_carpeta_user():
    carpeta_seleccionada = datos_usuario['ruta_pf']
    try:
        python_dir = pf_object.open_folder(carpeta_seleccionada)
        editar_output(f"Conexión exitosa: {carpeta_seleccionada}")
        etiqueta_conexion.configure(text=f"Conexión DigSilent: {python_dir}", foreground="green", font=("Arial", 12, "bold"))
    # ... some calculations ...
    except:
        editar_output(f"Error conexión PF: {carpeta_seleccionada}")      
def procesar_entrada():
    # Obtener el texto de la entrada
    entrada_texto = entrada.get("1.0", tk.END).strip()
    # Procesar la entrada como desees
    if entrada_texto:
        editar_output(f"TU: {entrada_texto}")
        # Borrar el contenido de la entrada después de procesarlo
        text_result = pdf_object.text_rule(entrada_texto)
        editar_output(f"GPT: {text_result}")
        entrada.delete("1.0", tk.END)
def mostra_pagina():
    text = "Mostrar la pagina {} del pdf"
    entrada.delete("1.0", tk.END)  # Borrar el contenido existente
    entrada.insert(tk.END, text)  # Insertar el nuevo texto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Revisión de Modelos con ChatGPT")

# Configurar columnas y filas para que se expandan con la ventana
ventana.columnconfigure(0, weight=5)
ventana.columnconfigure(1, weight=1)

ventana.rowconfigure(0, weight=0)  # Configurar la primera fila para que no cambie su tamaño vertical
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=0)  # Nueva fila para los textos "Archivo PDF" y "Conexión"

# Crear el menú superior con ttk
menubar = tk.Menu(ventana)
ventana.config(menu=menubar)

# Crear un menú desplegable llamado "Configuración" con ttk
menu_configuracion = tk.Menu(menubar, tearoff=0,)
menubar.add_cascade(label="Archivo PDF", menu=menu_configuracion)
# Agregar una opción al menú de configuración con ttk
menu_configuracion.add_command(label="Seleccionar archivo", command=seleccionar_archivo)

# Crear un menú desplegable llamado "Configuración" con ttk
menu_configuracion = tk.Menu(menubar, tearoff=0,)
menubar.add_cascade(label="Conexión Power Factory", menu=menu_configuracion)
# Agregar una opción al menú de configuración con ttk
menu_configuracion.add_command(label="Seleccionar carpeta", command=seleccionar_carpeta,)

if datos_usuario['ruta_pf']:
    python_dir = datos_usuario['ruta_pf'].split('/')[-2]+' V.'+datos_usuario['ruta_pf'].split('/')[-1]
    menu_configuracion.add_command(label=python_dir, command=seleccionar_carpeta_user)

## Menu funciones activas ---------------------------------------------------------------
# Crear un menú desplegable llamado "Configuración" con ttk
menu_functions = tk.Menu(menubar, tearoff=0,)
menubar.add_cascade(label="Funciones disponibles", menu=menu_functions)
# Agregar una opción al menú de configuración con ttk
menu_functions.add_command(label="Mostrar una pagina", command=mostra_pagina)
# Agregar una opción al menú de configuración con ttk
menu_functions.add_command(label="Mostrar una pagina", command=mostra_pagina)
## Menu funciones activas ---------------------------------------------------------------


# Crear la entrada como un widget Text
entrada = tk.Text(ventana, height=3, width=40)
entrada.grid(row=0, column=0, padx=(10, 0), pady=(20,0), sticky="nsew")  # sticky="nsew" para expandir en todas las direcciones

# Crear un botón para procesar la entrada
tamanio_fuente = Font(family="Helvetica", size=12)
boton_procesar = tk.Button(ventana, text="Procesar", font=tamanio_fuente, command=procesar_entrada)
boton_procesar.grid(row=0, column=1, padx=20, pady=(20,0), sticky="nsew")  # No configurar sticky para evitar cambio en tamaño vertical

# Crear la ventana de salida con una altura mayor
salida = tk.Text(ventana, height=40, width=110, state="disabled")
salida.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")  # sticky="nsew" para expandir en todas las direcciones

# Etiquetas al final de la ventana
etiqueta_pdf = ttk.Label(ventana, text="Sin Archivo PDF")
etiqueta_pdf.grid(row=2, column=0, padx=(10, 0), pady=5, sticky="w")

etiqueta_conexion = ttk.Label(ventana, text="Sin Conexión con PF")
etiqueta_conexion.grid(row=2, column=1, padx=(0, 10), pady=5, sticky="e")


# Permitir redimensionar la ventana
ventana.resizable(width=True, height=True)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
