import tkinter as tk
#### faltou fazer ele decodificar a mensagem que recebe

class MasterApp:

    def __init__(self, root):

        self.root = root # define a pg do master como a principal

        self.root.title("Master - Receptor")
        self.root.geometry("900x700")

        tk.Label(
            root,
            text="Master aguardando mensagens...",#mensagem de espera a recepção
            font=("Arial", 16)
        ).pack(pady=20)
        #mostra o recebido
        self.label_ami = tk.Label(
            root,
            text="AMI recebido:"
        )
        self.label_ami.pack()

        self.label_binary = tk.Label(
            root,
            text="Binário:"
        )
        self.label_binary.pack()

        self.label_cipher = tk.Label(
            root,
            text="Texto cifrado:"
        )
        self.label_cipher.pack()

        self.label_message = tk.Label(
            root,
            text="Mensagem final:"
        )
        self.label_message.pack()

#instancia o master
def run_master():

    root = tk.Tk()

    app = MasterApp(root)

    root.mainloop()


if __name__ == "__main__":
    run_master()