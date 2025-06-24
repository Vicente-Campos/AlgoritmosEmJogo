'''
DECLARAR FUNÇOES DE BOAS VINDAS E CODIGOS RELACIONADOS
'''
import os
import time

    
def limpar_terminal():
    """Limpa a tela do terminal, compatível com Windows e sistemas Unix."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        

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
