# Semana 13
# Tarea: Creación de una Aplicación GUI Básica

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Datos U.E.A.")

# Etiquetas y campos de texto
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_cedula = tk.Label(ventana, text="Cédula:")
label_cedula.grid(row=1, column=0, padx=5, pady=5)
entry_cedula = tk.Entry(ventana)
entry_cedula.grid(row=1, column=1, padx=5, pady=5)

label_semestre = tk.Label(ventana, text="Semestre:")
label_semestre.grid(row=2, column=0, padx=5, pady=5)
entry_semestre = tk.Entry(ventana)
entry_semestre.grid(row=2, column=1, padx=5, pady=5)

label_especialidad = tk.Label(ventana, text="Especialidad:")
label_especialidad.grid(row=3, column=0, padx=5, pady=5)
entry_especialidad = tk.Entry(ventana)
entry_especialidad.grid(row=3, column=1, padx=5, pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana)
lista_datos.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


# Función para agregar datos
def agregar_datos():
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    semestre = entry_semestre.get()
    especialidad = entry_especialidad.get()

    if nombre and cedula and semestre and especialidad:
        lista_datos.insert(tk.END, f"{nombre} - {cedula} - {semestre} - {especialidad}")
        entry_nombre.delete(0, tk.END)
        entry_cedula.delete(0, tk.END)
        entry_semestre.delete(0, tk.END)
        entry_especialidad.delete(0, tk.END)
    else:
        tk.messagebox.showwarning("Advertencia", "Debe completar todos los campos.")


# Función para limpiar datos
def limpiar_datos():
    lista_datos.delete(0, tk.END)


# Botones
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_datos)
boton_agregar.grid(row=4, column=0, padx=5, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.grid(row=4, column=1, padx=5, pady=5)

# Ejecutar la ventana
ventana.mainloop()

# Universidad Estatal Amazónica
# Andrés Ponce M.