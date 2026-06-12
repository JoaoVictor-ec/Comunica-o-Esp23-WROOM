import tkinter as tk

from master import run_master
from slave import run_slave


def start_interface():
#cria página inicial com botões para selecionar se o computador será a master ou slave.
    root = tk.Tk()

# janela de escolha do modd de operação master ou slave
    root.title("Comunicação de Dados")
    root.geometry("350x200")

    mode = tk.StringVar(value="master")

    tk.Label(
        root,
        text="Selecione o modo de operação",
        font=("Arial", 12, "bold")
    ).pack(pady=20)

    #botoes para escolha
    tk.Radiobutton(
        root,
        text="Master (Receptor)",
        variable=mode,
        value="master"
    ).pack()

    tk.Radiobutton(
        root,
        text="Slave (Transmissor)",
        variable=mode,
        value="slave"
    ).pack()

    def start():#seleciona a pagina a carregar baseado na escolga do botão

        selected = mode.get()

        root.destroy()

        if selected == "master":
            run_master()
        else:
            run_slave()

    tk.Button(# botão para confirmar envia de mensagem
        root,
        text="Iniciar",
        command=start,
        width=20
    ).pack(pady=20)

    root.mainloop()