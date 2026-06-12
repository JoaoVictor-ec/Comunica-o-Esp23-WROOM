# Será o módulo que enviará a mensagem para o esp que atua como master.

#biblioteca da interface
import tkinter as tk

#funções de codificação
from codification import (
    codification_cifra_cesar,
    word_to_bin,
    codification_AmiPseudoternario
)

#funções de conexão com a esp
from esp_funct import connect_esp, send_ami

#funções de gráficos
from grafics import generate_ami_tx_graphic
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SlaveApp:

    def __init__(self, root):

        # define a slave como janela principal ao escolhermos a slave como opção
        self.root = root

        # textinho pra mostrar o módulo
        self.root.title("Slave - Transmissor")
        self.root.geometry("1000x800")

        # verifica se há conexão com uma esp via serial
        try:
            self.esp = connect_esp()
            status = "ESP conectada"
        except Exception:
            self.esp = None
            status = "ESP não conectada"

        # define a fonte, pega uma mensagem usando um quadrado onde a pessoa pode escrever
        tk.Label(
            root,
            text=status,
            font=("Arial", 12)
        ).pack(pady=5)

        tk.Label(
            root,
            text="Mensagem"
        ).pack()

        # recebe entrada
        self.entry_message = tk.Entry(root, width=80)
        self.entry_message.pack(pady=5)

        # botão pra confirmar que a pessoa quer enviar a mensagem
        tk.Button(
            root,
            text="Enviar",
            command=self.process_message
        ).pack(pady=10)

        # configs de letras e textos pra deixar "bonito"
        self.label_cipher = tk.Label(
            root,
            text="Mensagem cifrada:"
        )
        self.label_cipher.pack(anchor="w", padx=10)

        self.label_binary = tk.Label(
            root,
            text="Binário:",
            wraplength=950,
            justify="left"
        )
        self.label_binary.pack(anchor="w", padx=10)

        self.label_ami = tk.Label(
            root,
            text="AMI:",
            wraplength=950,
            justify="left"
        )
        self.label_ami.pack(anchor="w", padx=10)

        # Parte do gráfico
        self.graph_frame = tk.Frame(root)
        self.graph_frame.pack(fill="both", expand=True, pady=10)

        self.canvas = None#garante que ao inicializar a tela não tera um gráfico vazio aparecendo lá

    def update_graph(self, ami):
        #carrega a figura retornada da função do grafico
        fig = generate_ami_tx_graphic(ami)

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg( # passa a fig para widget do tkinter
            fig,
            master=self.graph_frame
        )

        # mostra o gerado acima
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

        self.label_cipher.config(
            text=f"Mensagem cifrada: {cipher}"
        )

        self.label_binary.config(
            text=f"Binário: {binary}"
        )

        ami_text = str(ami)

        if len(ami_text) > 150:
            ami_text = ami_text[:150] + "..."

        self.label_ami.config(
            text=f"AMI: {ami_text}"
        )

        self.update_graph(ami)

        # se tiver conexão manda a codificação ami
        if self.esp:
            send_ami(self.esp, ami)
    # fecha cinexão com o esp se tiver alguma
    def close(self):

        if self.esp:
            self.esp.close()

        self.root.destroy()


def run_slave():#instancia a classe tk 

    root = tk.Tk()# janela do slave

    app = SlaveApp(root)

    root.protocol(
        "WM_DELETE_WINDOW",
        app.close
    )

    root.mainloop()


if __name__ == "__main__":
    run_slave()