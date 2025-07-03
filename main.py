# Importando funções utilitárias
from utils.funcoes import limpar_terminal, exibir_mensagens
import time

# Importando as funções principais de cada jogo
from jogos.forca.jogo_da_forca import jogar_forca
from jogos.pedra_papel_tesoura.jogo_ppt import jogar_ppt
from jogos.adivinhacao.adivinhacao import jogar_adivinhacao
from jogos.quiz.jogo_quiz import quiz

def exibir_menu_principal():
    """
    Exibe o menu principal do programa e gerencia a escolha do usuário para iniciar os jogos.
    """
    opcoes_menu = {
        '1': {"texto": "Forca", "funcao": jogar_forca},
        '2': {"texto": "Pedra, Papel e Tesoura", "funcao": jogar_ppt},
        '3': {"texto": "Adivinhação", "funcao": jogar_adivinhacao},
        '4': {"texto": "Quiz", "funcao": quiz},
        '5': {"texto": "Sair", "funcao": None} # 'None' indica que esta opção encerra o programa
    }

    while True:
        limpar_terminal()
        print("=" * 40)
        print(" MENU DE JOGOS ".center(40))
        print("=" * 40)
        for chave, valor in opcoes_menu.items():
            print(f"{chave}. {valor['texto']}")
        print("=" * 40)

        escolha = input("Escolha uma opção: ").strip()

        if escolha in opcoes_menu:
            if opcoes_menu[escolha]["funcao"]: # Se a opção tem uma função associada (não é 'Sair')
                limpar_terminal() 
                opcoes_menu[escolha]["funcao"]() # Chama a função do jogo selecionado
            else: # Opção 'Sair'
                time.sleep(1.5)
                limpar_terminal()
                break # Sai do loop do menu principal
        else:
            print("\nOpção inválida! Por favor, escolha uma das opções listadas.")
            time.sleep(1.5)

# exibir_mensagens(['Bem-vindo ao projeto:', 'Algoritmos em jogo'])
exibir_menu_principal()
# exibir_mensagens(['Obrigado por jogar!', 'Ate a proxima!'])