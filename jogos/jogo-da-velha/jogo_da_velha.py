def como_jogar_jogoDaVelha():
    """Exibe as regras do jogo Pedra, Papel e Tesoura e aguarda a interação do usuário."""
    limpar_terminal()
    print("=" * 60)
    print(" BEM-VINDO AO PEDRA, PAPEL E TESOURA ".center(60, "="))
    print("=" * 60)
    print("""
Regras do jogo:

Você jogará contra o seu oponente.
O jogo acontece em um tabuleiro de 3x3, com 9 espaços disponíveis.
Cada jogador escolhe um símbolo: X ou O.
Os jogadores se alternam fazendo suas jogadas, colocando seu símbolo em um espaço vazio do tabuleiro.
O objetivo do jogo é alinhar três símbolos iguais (X ou O) em uma das seguintes formas:
-Linha horizontal (qualquer uma das 3 linhas).
-Linha vertical (qualquer uma das 3 colunas).
-Linha diagonal (duas possibilidades: da esquerda superior à direita inferior ou da direita superior à esquerda inferior).

Condições de vitória:
Se um jogador conseguir alinhar 3 de seus símbolos, ele vence a partida!
Empate:
Se todos os 9 espaços forem preenchidos sem que nenhum jogador vença, o jogo termina em EMPATE.
""")
    input("Pressione Enter para começar o jogo...")
    
# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):n
    print("\n")
    for i in range(3):
        linha = " | ".join(tabuleiro[i])
        print(" " + linha)
        if i < 2:
            print("---+---+---")
    print("\n")

# Função para verificar vitória
def verificar_vitoria(tabuleiro, jogador):
    # Linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] == jogador:
            return True
    # Colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False
