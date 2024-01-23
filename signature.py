import hashlib
import rsa
import tkinter as tk

class App(tk.Frame):

  def __init__(self, master):
    super().__init__(master)
    self.master.title("Generador de firma digital")
    self.grid()

    self.data_label = tk.Label(self, text="Datos a firmar:")
    self.data_label.grid(row=0, column=0)

    self.data_entry = tk.Entry(self, width=50)
    self.data_entry.grid(row=0, column=1)

    self.generate_button = tk.Button(self, text="Generar firma", command=self.generate_signature)
    self.generate_button.grid(row=1, column=0)

    self.signature_label = tk.Label(self, text="Firma digital:")
    self.signature_label.grid(row=2, column=0)

    self.signature_entry = tk.Entry(self, width=50)
    self.signature_entry.grid(row=2, column=1)

    self.verify_button = tk.Button(self, text="Verificar firma", command=self.verify_signature)
    self.verify_button.grid(row=3, column=0)

    self.signature_valid_label = tk.Label(self, text="")
    self.signature_valid_label.grid(row=3, column=1)

  def generate_signature(self):
    # Generamos una clave privada y una clave pública.
    private_key, public_key = rsa.newkeys(2048)

    # Generamos una firma digital para los datos especificados.
    data = self.data_entry.get()
    signature = generate_signature(data, private_key)

    # Actualizamos la interfaz gráfica.
    self.signature_entry.delete(0, tk.END)
    self.signature_entry.insert(0, signature)

  def verify_signature(self):
    # Obtenemos los datos y la firma digital.
    data = self.data_entry.get()
    signature = self.signature_entry.get()

    # Verificamos la firma digital.
    if verify_signature(data, signature, public_key):
      self.signature_valid_label.configure(text="La firma es válida.")
    else:
      self.signature_valid_label.configure(text="La firma no es válida.")


root = tk.Tk()
app = App(root)
app.mainloop()