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
def imprimir_tabuleiro(tabuleiro):
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

# Função para verificar empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == " ":
                return False
    return True

# Função principal
def jogar_jogo_da_velha():
    print("=== Bem-vindo ao Jogo da Velha ===")
    print("Posições no tabuleiro:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nDigite o número da posição para fazer sua jogada.\n")

    # Tabuleiro vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        # Entrada do jogador
        posicao = input("Escolha uma posição (1 a 9): ")

        if not posicao.isdigit():
            print("❌ Entrada inválida. Digite um número de 1 a 9.")
            continue

        posicao = int(posicao)
        if posicao < 1 or posicao > 9:
            print("❌ Posição fora do intervalo. Escolha de 1 a 9.")
            continue

        linha = (posicao - 1) // 3
        coluna = (posicao - 1) % 3

        if tabuleiro[linha][coluna] != " ":
            print("⚠️ Essa posição já está ocupada. Tente outra.")
            continue

        # Marca a jogada
        tabuleiro[linha][coluna] = jogador_atual

        # Verifica vitória
        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"🏆 Jogador {jogador_atual} venceu! Parabéns!\n")
            break

        # Verifica empate
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("🤝 Deu velha! O jogo terminou em empate.\n")
            break

        # Alterna jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Inicia o jogo
jogar_jogo_da_velha()
