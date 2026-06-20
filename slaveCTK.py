import customtkinter as ctk

# Funções de codificação
from codification import (
    codification_cifra_cesar,
    word_to_bin,
    codification_AmiPseudoternario
)

# Funções de conexão com a esp
from esp_funct import find_esp, send_ami

# Funções de gráficos
from grafics import generate_ami_tx_graphic
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SlaveApp:

    def __init__(self, root, on_back_callback=None):
# define a slave como janela principal ao escolhermos a slave como opção
        self.root = root
        self.on_back_callback = on_back_callback

# textinho pra mostrar o módulo
        self.root.title("Slave - Transmissor")
        self.root.geometry("1000x800")

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

        # Verifica se há conexão com uma esp via serial
        try:
            self.esp = find_esp("SLAVE")
            status = "ESP conectada"
        except Exception:
            self.esp = None
            status = "ESP não conectada"

        # define a fonte, pega uma mensagem usando um quadrado onde a pessoa pode escrever
        ctk.CTkLabel(
            self.root,
            text=status,
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        ctk.CTkLabel(
            self.root,
            text="Mensagem:",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        # recebe entrada
        self.entry_message = ctk.CTkEntry(
            self.root, 
            placeholder_text="Digite a sua mensagem...",
            width=500,
        )
        self.entry_message.pack(pady=5)
        # botão pra confirmar que a pessoa quer enviar a mensagem
        ctk.CTkButton(
            self.root,
            text="Enviar",
            command=self.process_message,
            fg_color="#C850C0",
            hover_color="#4158D0",
            corner_radius=20,
            width=140,
            height=40
        ).pack(pady=10)

        # configs de letras e textos pra deixar "bonito"
        self.label_cipher = ctk.CTkLabel(
            self.root,
            text="Mensagem cifrada:",
            font=("Arial", 16, "bold")
        )
        self.label_cipher.pack(anchor="w", padx=20, pady=5)

        self.label_binary = ctk.CTkLabel(
            self.root,
            text="Binário:",
            wraplength=950,
            justify="left",
            font=("Arial", 16, "bold")
        )
        self.label_binary.pack(anchor="w", padx=20, pady=10)

        self.label_ami = ctk.CTkLabel(
            self.root,
            text="AMI:",
            wraplength=950,
            justify="left",
            font=("Arial", 16, "bold")
        )
        self.label_ami.pack(anchor="w", padx=20, pady=10)

        # Parte do gráfico
        self.graph_frame = ctk.CTkFrame(self.root)
        self.graph_frame.pack(fill="both", expand=True, pady=10, padx=20)

#garante que ao inicializar a tela não tera um gráfico vazio aparecendo lá
        self.canvas = None 

    def update_graph(self, ami):
        #carrega a figura retornada da função do grafico
        fig = generate_ami_tx_graphic(ami)

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

    def process_message(self):
    #chama as cdificações e mostra seus resultados
        message = self.entry_message.get()

        if not message:
            return

        cipher = codification_cifra_cesar(message)
        binary = word_to_bin(cipher)
        ami = codification_AmiPseudoternario(binary)

        self.label_cipher.configure(
            text=f"Mensagem cifrada: {cipher}"
        )

        self.label_binary.configure(
            text=f"Binário: {binary}"
        )

        ami_text = str(ami)
        if len(ami_text) > 150:
            ami_text = ami_text[:150] + "..."

        self.label_ami.configure(
            text=f"AMI: {ami_text}"
        )

        self.update_graph(ami)

        if self.esp:
            send_ami(self.esp, ami)

    def go_back(self):
        self.close()
        if self.on_back_callback:
            self.on_back_callback()

    def close(self):
        if self.esp:
            self.esp.close()
        try:
            self.root.destroy()
        except Exception:
            pass

def run_slave(on_back=None):#instancia a classe ctk 
    ctk.set_appearance_mode("dark")
    root = ctk.CTk() 

    app = SlaveApp(root, on_back_callback=on_back)#janela do slave

    root.protocol(
        "WM_DELETE_WINDOW",
        app.close
    )

    root.mainloop()

if __name__ == "__main__":
    run_slave()