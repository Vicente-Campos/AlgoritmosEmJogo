import os
import time
import random
from utils.funcoes import limpar_terminal, jogar_novamente

def como_jogar():
    """Exibe as regras do jogo de Adivinhação Numérica e aguarda a interação do usuário."""
    limpar_terminal()
    print("=" * 60)
    print(" BEM-VINDO AO JOGO DE ADIVINHAÇÃO NUMÉRICA ".center(60, "="))
    print("=" * 60)
    print("""
Regras do jogo:

- O computador escolherá um número secreto.
- Seu objetivo é adivinhar qual é esse número.
- A cada tentativa, o computador dirá se o seu palpite é "MAIOR" ou "MENOR" que o número secreto.
- O jogo possui dois modos distintos para você escolher.

Boa sorte!
""")
    input("Pressione Enter para começar o jogo...")
    limpar_terminal()

def escolher_modo_jogo():
    """
    Permite ao usuário escolher o modo de jogo e retorna os parâmetros correspondentes.
    Retorna uma tupla (limite_tentativas, min_numero, max_numero).
    """
    while True:
        limpar_terminal()
        print("=" * 60)
        print(" ESCOLHA O MODO DE JOGO ".center(60, "="))
        print("=" * 60)
        print("""
Modos disponíveis:

1 - Modo CLÁSSICO:
    - Número entre 1 e 100
    - Limite de 7 tentativas

2 - Modo DESAFIO:
    - Número entre 1 e 1000
    - Sem limite de tentativas (jogar até acertar!)

""")
        
        modo_input = input("Escolha o modo (1 ou 2): ")

        if modo_input.isdigit():
            modo = int(modo_input)
            if modo == 1:
                print("\nModo CLÁSSICO escolhido: 7 tentativas, número entre 1 e 100.")
                time.sleep(2.5)
                return 7, 1, 100 
            elif modo == 2:
                print("\nModo DESAFIO escolhido: Tentativas ilimitadas, número entre 1 e 1000.")
                time.sleep(2.5)
                return -1, 1, 1000 # -1 indica sem limite
            else:
                print("\nOpção inválida! Por favor, digite 1 ou 2.")
                input("Pressione Enter para tentar novamente...")
        else:
            print("\nEntrada inválida! Por favor, digite um número inteiro (1 ou 2).")
            input("Pressione Enter para tentar novamente...")

def obter_palpite(min_num, max_num, cabecalho_jogo_str):
    """
    Solicita e valida o palpite do jogador.
    Garante que a entrada seja um número inteiro válido dentro do range.
    Limpa o terminal e exibe o cabeçalho após mensagens de erro.
    """
    while True:
        palpite_input = input(f"Digite seu palpite (entre {min_num} e {max_num}): ")
        
        if palpite_input.isdigit():
            palpite = int(palpite_input)
            if min_num <= palpite <= max_num:
                return palpite
            else:
                print(f"Palpite fora do intervalo ({min_num}-{max_num}). Tente novamente.")
                time.sleep(1.5)
                limpar_terminal()
                print(cabecalho_jogo_str) 
        else:
            print("Entrada inválida! Por favor, digite apenas números inteiros.")
            time.sleep(1.5)
            limpar_terminal()
            print(cabecalho_jogo_str) 

def jogar_adivinhacao():
    """Controla o fluxo completo do jogo de Adivinhação Numérica."""
    
    while True: # Loop para permitir múltiplas partidas
        limpar_terminal()
        como_jogar()
        
        max_tentativas, min_numero, max_numero = escolher_modo_jogo()

        numero_secreto = random.randint(min_numero, max_numero)
        tentativas = 0
        acertou = False

        # Prepara o cabeçalho do jogo uma vez para reutilização
        cabecalho_do_jogo_str = (
            "=" * 50 + "\n" +
            " JOGO DE ADIVINHAÇÃO NUMÉRICA ".center(50, "=") + "\n" +
            f"Número secreto está entre {min_numero} e {max_numero}.".center(50) + "\n" +
            "=" * 50
        )

        while True: # Loop principal de tentativas
            # Condição de perda para modo limitado
            if max_tentativas != -1 and tentativas >= max_tentativas:
                break 
                
            limpar_terminal()
            print(cabecalho_do_jogo_str)

            # Exibe o número da tentativa, ajustando para o modo ilimitado
            if max_tentativas != -1:
                print(f"\nTentativa {tentativas + 1}/{max_tentativas}")
            else:
                print(f"\nTentativa {tentativas + 1}")
            print("-" * 30)

            # Obtém e valida o palpite do jogador
            palpite_jogador = obter_palpite(min_numero, max_numero, cabecalho_do_jogo_str)
            
            tentativas += 1

            # Verifica o palpite e dá dicas
            if palpite_jogador == numero_secreto:
                print(f"\nPARABÉNS! Você adivinhou o número {numero_secreto} em {tentativas} tentativas!")
                acertou = True
                time.sleep(5)
                break
            elif palpite_jogador < numero_secreto:
                print("\nO número secreto é MAIOR que o seu palpite.")
            else: 
                print("\nO número secreto é MENOR que o seu palpite.")
            
            time.sleep(2) 

        # Mensagens finais (vitória/derrota)
        if not acertou:
            limpar_terminal()
            print("=" * 50)
            print(" FIM DE JOGO ".center(50, "="))
            print("=" * 50)
            if max_tentativas != -1:
                print(f"\nVocê esgotou suas {max_tentativas} tentativas.")
            else: 
                print(f"\nVocê não conseguiu adivinhar o número.") 
            print(f"O número secreto era: {numero_secreto}")
            time.sleep(3)

        limpar_terminal()
        # Pergunta ao usuário se deseja jogar novamente
        if not jogar_novamente():
            limpar_terminal()
            break