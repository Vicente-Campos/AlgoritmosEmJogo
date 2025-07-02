'''
DECLARAÇÃO DE FUNÇÕES USADAS EM OUTRAS PARTES DO PROJETO
'''
import os        # Para interagir com o sistema operacional
import time      # Para controlar pausas no tempo
import sys       # Para controlar a saída de caracteres no terminal
import shutil    # Para obter a largura do terminal
import pyfiglet  # Para gerar texto grande (ASCII Art)

def limpar_terminal():
    """Limpa a tela do terminal, compatível com Windows e sistemas Unix."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def obter_largura_terminal():
    """Obtém a largura do terminal em caracteres."""
    return shutil.get_terminal_size().columns

def ler_arquivo_relativo(nome_arquivo):
    """
    Lê palavras de um arquivo de texto na pasta 'arquivos'.
    
    Acessa arquivos de forma **portátil** construindo o caminho relativo ao script atual,
    subindo um níveil ('..') para a pasta 'projeto_principal' e depois acessando 'arquivos'.
    Trata erros de arquivo não encontrado ou outros problemas de leitura, retornando uma lista vazia.
    """
    diretorio_do_script = os.path.dirname(__file__)
    caminho_para_arquivos = os.path.join(diretorio_do_script, '..', 'arquivos', nome_arquivo)
    caminho_final = os.path.abspath(caminho_para_arquivos)

    try:
        with open(caminho_final, 'r', encoding='utf-8') as f:
            # Filtra linhas vazias e remove espaços em branco de cada palavra.
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado em '{caminho_final}'")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return []
    

def jogar_novamente():
    """
    Pergunta ao usuário se deseja jogar novamente.
    
    Isola a lógica de validação da resposta 's' ou 'n' para reutilização.
    Retorna `True` para jogar novamente, `False` para sair.
    """
    while True:
        print("\n" + "=" * 40)
        print(" Deseja jogar novamente? ".center(40, "="))
        print("=" * 40)
        print(' S / N '.center(40, '='))
        print("\n" + "=" * 40)
        
        jogar_novamente_input = input("Resposta: ").upper().strip()

        if jogar_novamente_input == 'S':
            return True
        elif jogar_novamente_input == 'N':
            limpar_terminal()
            print("\n" + "=" * 40)
            print(" Obrigado por jogar! ".center(40, "="))
            print(" Até a próxima! ".center(40, "="))
            print("=" * 40)
            time.sleep(3) # Aumentei um pouco a pausa para a mensagem final ser bem lida
            return False
        else:
            print("\n" + "-" * 40)
            print(" Opção inválida! ".center(40))
            print(" Por favor, digite 'S' para sim ou 'N' para não. ".center(40))
            print("-" * 40)
            time.sleep(2.5) # Aumentei a pausa para o usuário ler o erro antes de repetir
            limpar_terminal()

def exibir_mensagens(mensagens: list[str]):
    """
    Exibe uma lista de mensagens como texto grande animado no terminal,
    usando configurações padrão.
    """
    # Configurações padrão para a animação
    FONTE_PADRAO = "ansi_shadow"
    ATRASO_CARACTERE_PADRAO = 0.010
    ATRASO_FRASE_PADRAO = 1.0

    largura_terminal = obter_largura_terminal() # Largura do terminal
    
    limpar_terminal()

    # Loop para exibir cada frase da lista com animação
    for i, frase in enumerate(mensagens):
        # Gera o texto grande, ajustando à largura do terminal
        texto_grande_ascii = pyfiglet.figlet_format(frase, font=FONTE_PADRAO, width=largura_terminal)

        # Exibe cada caractere do texto grande gradualmente
        for char in texto_grande_ascii:
            sys.stdout.write(char) # Escreve o caractere
            sys.stdout.flush()     # Exibe imediatamente
            time.sleep(ATRASO_CARACTERE_PADRAO) # Pausa para o efeito

        # Pausa entre frases, se houver mais de uma
        if i < len(mensagens) - 1:
            sys.stdout.flush()
            time.sleep(ATRASO_FRASE_PADRAO)

    sys.stdout.flush()
    time.sleep(1.5)
    if mensagens[0] == 'Bem-vindo ao projeto:': input('Pressione Enter para continuar...')
    limpar_terminal()