import tkinter as tk
from tkinter import filedialog, messagebox

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("800x600")
        # Crear area de texto
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill="both")
        # Crear menú
        self.crear_menu()

    def crear_menu(self):
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.salir)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        self.config(menu=menu_bar)

    def abrir_archivo(self):
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Todos los archivos", "*.*")])
        if not ruta_archivo:
            return
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, contenido)
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {e}")

    def guardar_archivo(self):
        ruta_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Todos los archivos", "*.*")])
        if not ruta_archivo:
            return
        try:
            contenido = self.text_area.get("1.0", tk.END)
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el archivo: {e}")

    def salir(self):
        self.quit()  # <- Este método cierra la ventana

if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()