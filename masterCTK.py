import customtkinter as ctk

from grafics import generate_ami_rx_graphic

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from esp_funct import find_esp, receive_ami

from codification import (
    decodification_AmiPseudoternario,
    bin_to_word,
    decodification_cifra_cesar
)

class MasterApp:

    def __init__(self, root, on_back_callback=None):

        self.root = root 
        self.on_back_callback = on_back_callback

        #tenta conectar com a esp
        self.esp = find_esp("MASTER")

        if self.esp:
            status = "ESP conectada"
        else:
            status = "ESP não conectada"


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

        self.label_status = ctk.CTkLabel(
            self.root,
            text=status,
            font=("Arial", 14, "bold")
        )

        self.label_status.pack(pady=10)

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

        # Área do gráfico
        self.graph_frame = ctk.CTkFrame(self.root)
        self.graph_frame.pack(
            fill="both",
            expand=True,
            pady=10,
            padx=20
        )

        self.canvas = None
        
        self.check_serial()

    def close(self):#função que fecha conexão com o esp, necessário caso queira mudar a função do pc
        if self.esp:
            self.esp.close()

        self.root.destroy()

    def go_back(self):
                # Fecha a janela atual e chama a função para recriar o menu inicial

        if self.esp:
            self.esp.close()

        self.root.destroy()

        if self.on_back_callback:
            self.on_back_callback()
    def update_graph(self, ami):

        fig = generate_ami_rx_graphic(ami)

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(
            fig,
            master=self.graph_frame
        )

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    def check_serial(self):

        if self.esp is None:
            self.root.after(1000, self.check_serial)
            return

        if self.esp:

            ami = receive_ami(self.esp)

            if ami:
                self.process_received_ami(ami)

        self.root.after(100, self.check_serial)

    def process_received_ami(self, ami):

        self.update_graph(ami)#grifco
        # Mostra o AMI recebido
        self.label_ami.configure(
            text=f"AMI recebido:\n{ami}"
        )

        # Decodifica AMI -> binário
        binary = decodification_AmiPseudoternario(ami)

        self.label_binary.configure(
            text=f"Binário:\n{binary}"
        )

        # Binário -> texto cifrado
        cipher_text = bin_to_word(binary)

        self.label_cipher.configure(
            text=f"Texto cifrado:\n{cipher_text}"
        )

        # César inversa
        original_text = decodification_cifra_cesar(cipher_text)

        self.label_message.configure(
            text=f"Mensagem final:\n{original_text}"
        )

# Janela
def run_master(on_back=None):

    ctk.set_appearance_mode("dark")

    root = ctk.CTk()

    app = MasterApp(
        root,
        on_back_callback=on_back
    )

    root.protocol(
        "WM_DELETE_WINDOW",
        app.close
    )

    root.mainloop()

if __name__ == "__main__":
    run_master()