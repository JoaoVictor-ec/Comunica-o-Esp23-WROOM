from matplotlib.figure import Figure

def generate_ami_tx_graphic(local_data):
    """
    Generates an isolated graph of the transmission AMI signal.
    To be used on the PC that is SENDING the message.
    """
    # estende a imagem em um bit pra aparecer completo o gráfico
    x_axis = list(range(len(local_data) + 1))
    local_data_plot = local_data + [local_data[-1]]

    # ajusta dimensões e detalhes do gráfico
    fig = Figure(figsize=(8, 3), dpi=100)

    # numero do plot
    ax = fig.add_subplot(1, 1, 1)

    # ajusta infos dos eixos
    ax.step(x_axis, local_data_plot, where='post', color='#1f77b4', linewidth=2)
    ax.set_title('Transmission: Pseudoternary AMI Signal')
    ax.set_ylabel('Voltage (V)')
    ax.set_xlabel('Bit Index')
    ax.set_ylim(-1.5, 1.5)
    ax.set_yticks([-1, 0, 1])
    
    # Define os números do eixo X para cada bit
    ax.set_xticks(x_axis[:-1])
    #Diminui a fonte do eixo X para tamanho 8
    ax.tick_params(axis='x', labelsize=8)
    
    ax.grid(True, linestyle='--', alpha=0.6)

    fig.tight_layout()
    return fig


def generate_ami_rx_graphic(esp_data):
    """
    Generates an isolated graph of the reception AMI signal.
    To be used on the PC that is RECEIVING the message via ESP.
    """
    # estende a imagem em um bit pra aparecer completo o gráfico
    x_axis = list(range(len(esp_data) + 1))
    esp_data_plot = esp_data + [esp_data[-1]]

    # ajusta dimensões e detalhes do gráfico
    fig = Figure(figsize=(8, 3), dpi=100)

    # numero do plot
    ax = fig.add_subplot(1, 1, 1)

    # ajusta infos dos eixos
    ax.step(x_axis, esp_data_plot, where='post', color='#ff7f0e', linewidth=2)
    ax.set_title('Reception: Signal Received via ESP')
    ax.set_ylabel('Voltage (V)')
    ax.set_xlabel('Bit Index')
    ax.set_ylim(-1.5, 1.5)
    ax.set_yticks([-1, 0, 1])
    
    # Define os números do eixo X para cada bit
    ax.set_xticks(x_axis[:-1])
    # Diminui a fonte do eixo X para tamanho 8
    ax.tick_params(axis='x', labelsize=8)
    
    ax.grid(True, linestyle='--', alpha=0.6)

    fig.tight_layout()
    return fig
