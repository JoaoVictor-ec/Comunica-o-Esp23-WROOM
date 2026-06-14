import customtkinter as ctk
from masterCTK import run_master
from slaveCTK import run_slave

def start_interface():

    # Cria a janela 
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.title("Comunicação de Dados")
    root.geometry("500x400")

    # Inicia sem botões selecionados 
    mode = ctk.StringVar(value="")

    # Textinho superior
    ctk.CTkLabel(
        master=root,
        text="Selecione o modo de operação",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    # Botão de seleção MASTER
    ctk.CTkRadioButton(
        master=root,
        text="Master (Receptor)",
        fg_color="#C850C0",
        hover_color="#4158D0",
        variable=mode,
        value="master"
    ).pack(pady=15)

    # Botão de seleção SLAVE
    ctk.CTkRadioButton(
        master=root,
        text="Slave (Transmissor)",
        fg_color="#C850C0",
        hover_color="#4158D0",
        variable=mode,
        value="slave"
    ).pack(pady=15)

    def start():
        selected = mode.get()
        
        # Verifica se não foi slecionado nenhum botão
        if selected == "":
            return 
            
        root.destroy()

        # Redireciona de acordo com o botão selecionado
        if selected == "master":
            run_master(on_back=start_interface)
        elif selected == "slave":
            run_slave(on_back=start_interface)

    # Botão de iniciar
    ctk.CTkButton(
        master=root,
        text="Iniciar", 
        command=start,
        corner_radius=32,
        fg_color="#C850C0",
        hover_color="#4158D0"
    ).pack(pady=15)

    root.mainloop()