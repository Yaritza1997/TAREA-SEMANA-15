import tkinter as tk
from tkinter import messagebox

# Función para añadir tareas
def add_task():
    task = task_entry.get()  # Obtener el texto de la entrada
    if task != "":  # Si la entrada no está vacía
        task_listbox.insert(tk.END, task)  # Añadir la tarea a la lista
        task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")  # Mostrar un mensaje si no hay tarea

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
        task_listbox.itemconfig(selected_task_index, {'bg':'lightgreen'})  # Cambiar el fondo de la tarea a verde claro
    except IndexError:
        messagebox.showwarning("Sin selección", "Por favor, seleccione una tarea para marcar como completada.")  # Mensaje si no se selecciona tarea

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
        task_listbox.delete(selected_task_index)  # Eliminar la tarea seleccionada
    except IndexError:
        messagebox.showwarning("Sin selección", "Por favor, seleccione una tarea para eliminar.")  # Mensaje si no se selecciona tarea

# Función para manejar la tecla Enter en el campo de entrada
def on_enter_pressed(event):
    add_task()  # Llamar a la función de añadir tarea al presionar Enter

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x300")  # Aumentar el tamaño de la ventana

# Crear la entrada para agregar nuevas tareas
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Crear los botones de la aplicación
add_button = tk.Button(root, text="Añadir Tarea", width=15, command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

mark_button = tk.Button(root, text="Marcar como Completada", width=20, command=mark_completed)
mark_button.grid(row=1, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
delete_button.grid(row=1, column=1, padx=10, pady=10)

# Crear la lista para mostrar las tareas
task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Vincular la tecla Enter al campo de entrada
task_entry.bind("<Return>", on_enter_pressed)

# Ejecutar la aplicación
root.mainloop()
