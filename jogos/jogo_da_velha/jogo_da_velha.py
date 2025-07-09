from utils.funcoes import limpar_terminal
import time

def como_jogar_jogoDaVelha():
    """Exibe as regras do jogo da velha e aguarda a interação do usuário."""
    limpar_terminal()
    print("=" * 60)
    print(" BEM-VINDO AO JOGO DA VELHA ".center(60, "="))
    print("=" * 60)
    print("""
Regras do jogo:

Você jogará contra outro jogador alternando entre X e O.
O jogo acontece em um tabuleiro de 3x3, com 9 espaços disponíveis.
Cada jogador escolhe uma posição numerada de 1 a 9 para colocar seu símbolo.

O objetivo do jogo é alinhar três símbolos iguais (X ou O) em:
- Linha horizontal (qualquer uma das 3 linhas)
- Linha vertical (qualquer uma das 3 colunas)
- Linha diagonal (as duas diagonais possíveis)

Condições de vitória:
- O primeiro jogador a alinhar 3 símbolos iguais vence!
- Se todas as posições forem preenchidas sem um vencedor, é empate.
""")
    input("\nPressione Enter para começar o jogo...")
    limpar_terminal()

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro atual formatado"""
    print("\n  1 | 2 | 3")
    print(" -----------")
    print("  4 | 5 | 6")
    print(" -----------")
    print("  7 | 8 | 9\n")
    
    print(" " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("---+---+---")
    print(" " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("---+---+---")
    print(" " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2] + "\n")

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador atual venceu"""
    # Verifica linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    
    # Verifica colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False

def verificar_empate(tabuleiro):
    """Verifica se o jogo terminou em empate"""
    return all(celula != " " for linha in tabuleiro for celula in linha)

def jogar_jogo_da_velha():
    """Função principal que controla o fluxo do jogo"""
    while True:  # Loop para jogar novamente
        como_jogar_jogoDaVelha()
        
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        jogador_atual = "X"
        historico_jogadas = []
        
        while True:  # Loop da partida
            limpar_terminal()
            print(f"=== JOGO DA VELHA - Jogador {jogador_atual} ===")
            imprimir_tabuleiro(tabuleiro)
            
            # Mostra histórico de jogadas
            if historico_jogadas:
                print("Histórico:")
                for i, (jogador, pos) in enumerate(historico_jogadas, 1):
                    print(f"{i}. Jogador {jogador} jogou na posição {pos}")
                print()
            
            # Validação da jogada
            while True:
                try:
                    posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): "))
                    if posicao < 1 or posicao > 9:
                        print("Posição inválida. Escolha um número entre 1 e 9.")
                        continue
                        
                    linha = (posicao - 1) // 3
                    coluna = (posicao - 1) % 3
                    
                    if tabuleiro[linha][coluna] != " ":
                        print("Esta posição já está ocupada. Escolha outra.")
                        continue
                        
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número entre 1 e 9.")
            
            # Executa a jogada
            tabuleiro[linha][coluna] = jogador_atual
            historico_jogadas.append((jogador_atual, posicao))
            
            # Verifica vitória
            if verificar_vitoria(tabuleiro, jogador_atual):
                limpar_terminal()
                imprimir_tabuleiro(tabuleiro)
                print(f"🎉 PARABÉNS! Jogador {jogador_atual} venceu! 🎉")
                break
                
            # Verifica empate
            if verificar_empate(tabuleiro):
                limpar_terminal()
                imprimir_tabuleiro(tabuleiro)
                print("🤝 EMPATE! O jogo terminou sem vencedores. 🤝")
                break
                
            # Alterna jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
        
        # Pergunta se quer jogar novamente
        while True:
            resposta = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
            if resposta in ("S", "N"):
                break
            print("Por favor, digite 'S' para Sim ou 'N' para Não.")
        
        if resposta == "N":
            print("\nObrigado por jogar! Voltando ao menu principal...")
            time.sleep(2)
            limpar_terminal()
            return  # Retorna ao menu principal