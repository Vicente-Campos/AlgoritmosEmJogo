import time   # Para controlar pausas no jogo
import random # Para escolher palavras aleatoriamente
from utils.funcoes import limpar_terminal, ler_arquivo_relativo, jogar_novamente # Importa funções utilitárias essenciais do módulo 'funcoes' dentro do pacote 'utils'.

## Funções de Utilitário

def como_jogar():
    """Exibe as regras do jogo e pausa para o usuário iniciar."""
    limpar_terminal()
    print("=" * 60)
    print(" BEM-VINDO AO JOGO DA FORCA ".center(60, "="))
    print("=" * 60)
    print("""
Regras do jogo:

- Você deve adivinhar a palavra secreta letra por letra.
- A cada letra errada, você perde uma tentativa.
- Se errar muitas vezes, o boneco será enforcado!
- Se descobrir todas as letras antes disso, você vence!

Boa sorte!
""")
    input("Pressione Enter para começar o jogo...")

## Funções de Lógica do Jogo

def categoria_palavra():
    """
    Permite ao usuário escolher uma categoria de palavras.
    
    Usa um loop 'while True' para **validar a entrada**, garantindo que o usuário
    digite um número inteiro entre 1 e 5.
    """
    while True:
        limpar_terminal()
        print("=" * 60)
        print(" Escolha uma das seguintes categorias para iniciar ".center(60, "="))
        print("=" * 60)
        print("""
Categorias:

1 - Animais
2 - Objetos
3 - Lugares
4 - Filmes
5 - Esportes
""")
        
        categoria_input = input("Escolha: ")

        if categoria_input.isdigit():
            categoria = int(categoria_input)
            if 1 <= categoria <= 5:
                return categoria # Retorna a categoria e encerra o loop
            else:
                print("\nOpção inválida! Por favor, digite 1, 2, 3, 4 ou 5.")
                input("Pressione Enter para tentar novamente...")
        else:
            print("\nEntrada inválida! Por favor, digite um número inteiro.")
            input("Pressione Enter para tentar novamente...")

def palavra_secreta(categoria):
    """
    Seleciona uma palavra secreta aleatória com base na categoria.
    
    Centraliza a lógica de **carregamento de palavras** usando `ler_arquivo_relativo`.
    Lida com o cenário onde nenhuma palavra pode ser carregada, retornando `None`.
    """
    nome_arquivo = ""
    match categoria: # Usa 'match' para mapear a categoria escolhida ao nome do arquivo.
        case 1:
            nome_arquivo = "animais.txt"
        case 2:
            nome_arquivo = "objetos.txt"
        case 3:
            nome_arquivo = "lugares.txt"
        case 4:
            nome_arquivo = 'filmes.txt'
        case 5:
            nome_arquivo = 'esportes.txt'
        case _:
            print("Erro interno: Categoria inválida selecionada.")
            return None 

    palavras_da_categoria = ler_arquivo_relativo(nome_arquivo)

    if not palavras_da_categoria: # Verifica se a lista de palavras está vazia.
        print(f"Não foi possível carregar palavras da categoria '{nome_arquivo}'.")
        print("Verifique se o arquivo existe e contém palavras.")
        return None

    palavra_escolhida = random.choice(palavras_da_categoria).upper()
    return palavra_escolhida

def desenhar_forca(tentativas):
    """Exibe o desenho da forca com base no número de erros do jogador."""
    forcas = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(forcas[tentativas])


## Função Principal do Jogo

def jogar_forca():
    """
    Controla o fluxo completo do jogo da forca, desde a seleção da categoria
    até o fim da partida e a opção de jogar novamente.
    """
    while True: # Loop principal para permitir múltiplas partidas consecutivas.
        limpar_terminal()
        como_jogar()
        
        categoria = categoria_palavra()
        palavra = palavra_secreta(categoria)
        
        if palavra is None: # Trata o caso de falha ao carregar a palavra secreta.
            print("Não foi possível iniciar o jogo devido a um erro na seleção da palavra.")
            time.sleep(2)
            continue # Reinicia o loop principal para escolher a categoria novamente.

        limpar_terminal()

        # Inicializa o estado do jogo para a nova partida.
        palavra_escondida = ["_" for _ in palavra]
        letras_erradas = []
        tentativas_restantes = 6
        
        mostrar_categoria = {1: 'Animal', 2: 'Objeto', 3: 'Lugar', 4: 'Filme', 5: 'Esporte'}

        while tentativas_restantes > 0: # Loop interno: uma rodada da forca.
            limpar_terminal()
            print("=" * 50)
            print(" JOGO DA FORCA ".center(50, "="))
            print("=" * 50)
            print(f'\nCategoria: {mostrar_categoria[categoria]}')
            print("Palavra: " + " ".join(palavra_escondida))
            print(f"Letras erradas: {', '.join(letras_erradas)}")
            desenhar_forca(6 - tentativas_restantes) # O argumento indica o número de erros atuais.

            if "_" not in palavra_escondida: # Condição de vitória.
                print(f"\nPARABÉNS! Você acertou a palavra: {palavra}!")
                time.sleep(3)
                limpar_terminal()
                break # Sai do loop interno (fim da rodada atual).

            tentativa = input("Digite uma letra: ").upper()

            # Validação da entrada do usuário para garantir uma única letra.
            if not tentativa.isalpha() or len(tentativa) != 1:
                print("Entrada inválida. Digite apenas uma letra.")
                time.sleep(1.5)
                continue

            # Verifica se a letra já foi tentada.
            if tentativa in palavra_escondida or tentativa in letras_erradas:
                print(f"Você já tentou a letra '{tentativa}'. Tente outra!")
                time.sleep(1.5)
                continue

            # Processa a tentativa: correta ou errada.
            if tentativa in palavra:
                print(f"Boa! A letra '{tentativa}' está na palavra.")
                for i, letra_secreta in enumerate(palavra):
                    if letra_secreta == tentativa:
                        palavra_escondida[i] = tentativa # Revela a letra.
            else:
                print(f"Ops! A letra '{tentativa}' não está na palavra.")
                letras_erradas.append(tentativa)
                tentativas_restantes -= 1

            time.sleep(1.5) # Pausa breve para o jogador ver o resultado da tentativa.

        else: # Este 'else' é executado apenas se o loop interno terminar por esgotar tentativas (derrota).
            limpar_terminal()
            print("=" * 50)
            print(" JOGO DA FORCA ".center(50, "="))
            print("=" * 50)
            desenhar_forca(6) # Desenha a forca completa.
            print(f"\nVOCÊ PERDEU! A palavra era: {palavra}")
            time.sleep(4) # Pausa para a mensagem de derrota.
            limpar_terminal()

        # Decide se o jogo continua com base na resposta do usuário.
        if not jogar_novamente():
            limpar_terminal() # Limpa o terminal antes de sair.
            break # Sai do loop principal, encerrando a função jogar_forca().