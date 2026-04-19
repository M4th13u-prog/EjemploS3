import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

# -------- CONFIG --------
ARCHIVO = "citas.json"

servicios = {
    "Corte de cabello": 20,
    "Manicure": 15,
    "Pedicure": 18,
    "Tinte": 40
}

citas = []

# -------- ARCHIVO --------

def guardar():
    with open(ARCHIVO, "w") as f:
        json.dump(citas, f)

def cargar():
    global citas
    try:
        with open(ARCHIVO, "r") as f:
            citas = json.load(f)
    except:
        citas = []

# -------- FUNCIONES --------

def registrar():
    nombre = entry_nombre.get()
    hora = entry_hora.get()
    servicio = servicio_var.get()

    if not nombre or not hora:
        messagebox.showerror("Error", "Complete todos los campos")
        return

    fecha = datetime.now().strftime("%d/%m/%Y")

    cita = {
        "cliente": nombre,
        "servicio": servicio,
        "precio": servicios[servicio],
        "hora": hora,
        "fecha": fecha,
        "estado": "Pendiente"
    }

    citas.append(cita)
    guardar()
    actualizar()

    entry_nombre.delete(0, tk.END)
    entry_hora.delete(0, tk.END)

def actualizar():
    lista.delete(0, tk.END)
    for c in citas:
        texto = f"{c['cliente']} | {c['servicio']} | S/ {c['precio']} | {c['hora']} | {c['estado']}"
        lista.insert(tk.END, texto)

def atender():
    try:
        i = lista.curselection()[0]
        citas[i]["estado"] = "Atendido"
        guardar()
        actualizar()
    except:
        messagebox.showerror("Error", "Seleccione una cita")

def eliminar():
    try:
        i = lista.curselection()[0]
        citas.pop(i)
        guardar()
        actualizar()
    except:
        messagebox.showerror("Error", "Seleccione una cita")

def buscar():
    nombre = entry_buscar.get().lower()
    lista.delete(0, tk.END)

    for c in citas:
        if nombre in c["cliente"].lower():
            lista.insert(tk.END, f"{c['cliente']} | {c['servicio']} | {c['hora']}")

def reporte():
    total = 0
    hoy = datetime.now().strftime("%d/%m/%Y")

    for c in citas:
        if c["fecha"] == hoy and c["estado"] == "Atendido":
            total += c["precio"]

    messagebox.showinfo("Reporte Diario", f"Ingresos de hoy: S/ {total}")

# -------- INTERFAZ --------

root = tk.Tk()
root.title("Beauty App PRO")
root.geometry("600x550")

tk.Label(root, text="Nombre").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Hora").pack()
entry_hora = tk.Entry(root)
entry_hora.pack()

tk.Label(root, text="Servicio").pack()
servicio_var = tk.StringVar()
servicio_var.set(list(servicios.keys())[0])

tk.OptionMenu(root, servicio_var, *servicios.keys()).pack()

tk.Button(root, text="Registrar", command=registrar, bg="green", fg="white").pack(pady=5)

# Lista
lista = tk.Listbox(root, width=80)
lista.pack(pady=10)

tk.Button(root, text="Atender", command=atender).pack()
tk.Button(root, text="Eliminar", command=eliminar).pack()

# Buscar
tk.Label(root, text="Buscar cliente").pack()
entry_buscar = tk.Entry(root)
entry_buscar.pack()

tk.Button(root, text="Buscar", command=buscar).pack()

# Reporte
tk.Button(root, text="Reporte Diario 💰", command=reporte, bg="blue", fg="white").pack(pady=10)

# -------- INICIO --------

cargar()
actualizar()

root.mainloop()