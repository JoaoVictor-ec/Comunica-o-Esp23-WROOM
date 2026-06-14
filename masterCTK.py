import customtkinter as ctk

class MasterApp:

    def __init__(self, root, on_back_callback=None):
        self.root = root 
        self.on_back_callback = on_back_callback
        self.root.title("Master - Receptor")
        self.root.geometry("900x700")

        # Botão de Voltar
        ctk.CTkButton(
            self.root,
            text="← Voltar para o Início",
            command=self.go_back,
            fg_color="transparent",
            text_color="#C850C0",
            hover_color="#2b2b2b",
            width=150,
            height=30
        ).pack(anchor="nw", padx=10, pady=10)

        ctk.CTkLabel(
            self.root,
            text="Master aguardando mensagens...",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        self.label_ami = ctk.CTkLabel(
            self.root,
            text="AMI recebido:",
            font=("Arial", 16, "bold")
        )
        self.label_ami.pack(anchor="w", padx=20, pady=10)

        self.label_binary = ctk.CTkLabel(
            self.root,
            text="Binário:",
            font=("Arial", 16, "bold")
        )
        self.label_binary.pack(anchor="w", padx=20, pady=10)

        self.label_cipher = ctk.CTkLabel(
            self.root,
            text="Texto cifrado:",
            font=("Arial", 16, "bold")
        )
        self.label_cipher.pack(anchor="w", padx=20, pady=10)

        self.label_message = ctk.CTkLabel(
            self.root,
            text="Mensagem final:",
            font=("Arial", 16, "bold")
        )
        self.label_message.pack(anchor="w", padx=20, pady=10)

    def go_back(self):
        # Fecha a janela atual e chama a função para recriar o menu inicial
        self.root.destroy()
        if self.on_back_callback:
            self.on_back_callback()

# Janela
def run_master(on_back=None):
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = MasterApp(root, on_back_callback=on_back)
    root.mainloop()

if __name__ == "__main__":
    run_master()