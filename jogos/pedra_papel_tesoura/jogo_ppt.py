import random # Necessário para a escolha aleatória do computador
import time   # Necessário para pausas visuais
from utils.funcoes import limpar_terminal, jogar_novamente # Importa funções utilitárias essenciais do módulo 'funcoes' dentro do pacote 'utils'.


def como_jogar_ppt():
    """Exibe as regras do jogo Pedra, Papel e Tesoura e aguarda a interação do usuário."""
    limpar_terminal()
    print("=" * 60)
    print(" BEM-VINDO AO PEDRA, PAPEL E TESOURA ".center(60, "="))
    print("=" * 60)
    print("""
Regras do jogo:

- Você jogará contra o computador.
- Ambos escolhem entre PEDRA, PAPEL ou TESOURA.
- As regras de vitória são:
    - PEDRA quebra TESOURA (PEDRA vence!)
    - PAPEL cobre PEDRA (PAPEL vence!)
    - TESOURA corta PAPEL (TESOURA vence!)
- Se vocês escolherem o mesmo, é um EMPATE!

Boa sorte!
""")
    input("Pressione Enter para começar o jogo...")
    limpar_terminal() # Limpa a tela após o usuário ler as regras

def escolha_jogada():
    """
    Solicita e valida a jogada do jogador (Pedra, Papel ou Tesoura).
    Garante que a entrada seja um número válido (1, 2 ou 3).
    """
    while True: # Loop para garantir uma entrada válida
        limpar_terminal()
        print("=" * 60)
        print(" Escolha uma das seguintes jogadas ".center(60, "="))
        print("=" * 60)
        print("""
Jogadas possíveis:

1 - PEDRA
2 - PAPEL
3 - TESOURA

""")
        
        jogada_input = input("Escolha: ")

        if jogada_input.isdigit():
            jogada = int(jogada_input)
            if 1 <= jogada <= 3:
                return jogada # Retorna a escolha válida e sai da função
            else:
                print("\nOpção inválida! Por favor, digite 1, 2 ou 3.")
                input("Pressione Enter para tentar novamente...")
        else:
            print("\nEntrada inválida! Por favor, digite um número inteiro.")
            input("Pressione Enter para tentar novamente...")

def jogar_ppt():
    """
    Controla o fluxo completo do jogo Pedra, Papel e Tesoura.
    Gerencia as jogadas do jogador e do computador, determina o vencedor e permite jogar múltiplas partidas.
    """
    opcoes = ["PEDRA", "PAPEL", "TESOURA"] # Define as jogadas possíveis para o jogo

    while True: # Loop principal para permitir múltiplas partidas consecutivas
        limpar_terminal()
        como_jogar_ppt() # Apresenta as regras no início de cada nova partida

        print("=" * 50)
        print(" PEDRA, PAPEL E TESOURA ".center(50, "="))
        print("=" * 50)

        # Obtém a jogada do jogador e a converte para o formato de texto (PEDRA, PAPEL, TESOURA)
        escolha_jogador = opcoes[escolha_jogada() - 1]

        escolha_computador = random.choice(opcoes) # Computador faz sua escolha aleatória

        print(f"\nVocê escolheu: {escolha_jogador}")
        print(f"O computador escolheu: {escolha_computador}")
        time.sleep(1.5) # Pausa para suspense e visualização

        # Lógica para determinar o vencedor da rodada
        if escolha_jogador == escolha_computador:
            print("\nRESULTADO: EMPATE!")
        elif (escolha_jogador == "PEDRA" and escolha_computador == "TESOURA") or \
             (escolha_jogador == "PAPEL" and escolha_computador == "PEDRA") or \
             (escolha_jogador == "TESOURA" and escolha_computador == "PAPEL"):
            print("\nRESULTADO: VOCÊ VENCEU!")
        else:
            print("\nRESULTADO: VOCÊ PERDEU!")

        time.sleep(2.5) # Pausa para o resultado ser lido
        limpar_terminal()

        # Pergunta ao usuário se deseja jogar novamente, usando a função utilitária
        if not jogar_novamente():
            limpar_terminal() # Limpa o terminal antes de encerrar o programa
            break # Sai do loop principal, encerrando a função jogar_ppt()