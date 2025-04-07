import tkinter as tk
from tkinter import messagebox

class AdminWindow:
    def __init__(self, master, usuario):
        self.master = master
        self.master.title("Tkinder Admin Panel")
        self.master.geometry("400x300")

        tk.Label(master, text=f"Bienvenido, {usuario} (Admin)", font=("Arial", 14)).pack(pady=10)

        tk.Button(master, text="Ver todos los usuarios", command=self.ver_usuarios).pack(pady=5)
        tk.Button(master, text="Cerrar", command=self.master.destroy).pack(pady=5)

    def ver_usuarios(self):
        try:
            with open("usuarios.json", "r") as f:
                import json
                usuarios = json.load(f)
            mensaje = "\n".join([f"{u} - {data['email']}" for u, data in usuarios.items()])
            messagebox.showinfo("Usuarios Registrados", mensaje)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar usuarios: {e}")
