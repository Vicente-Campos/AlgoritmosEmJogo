import json
import os
import random

def introducao():
    limpar_terminal()
    print("🎮 BEM-VINDO AO QUIZ 🎮\n")
    print("REGRAS DO JOGO:")
    print("- Você escolherá uma área de conhecimento: Geografia, História, Ciências ou Literatura.")
    print("- Depois, selecione o nível de dificuldade: Fácil, Médio ou Difícil.")
    print("- Cada pergunta vale 10 pontos.")
    print("- Responda com a letra correta da opção (A, B, C ou D).")
    print("- No final, sua pontuação será salva e você verá o ranking dos melhores jogadores!")
    print("\nBoa sorte! 🍀\n")


def limpar_terminal():
    """Limpa a tela do terminal, compatível com Windows e sistemas Unix."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def quiz(): #função principal
    input("Pressione ENTER para começar o jogo...\n").upper()
    print()
    
    nome = input("Digite seu nome: ")
    final_jogo(nome)


def escolher_area(): #função para escolher área
    print("🔍 Escolha uma área de conhecimento:")
    print("1 - Geografia 🌍")
    print("2 - História 🏰")
    print("3 - Ciências 🧪")
    print("4 - Literatura 📖")
    print()

    opcao = input("Digite o número da área escolhida: ")
    print()

    if opcao == "1":
        return "geografia"
    elif opcao == "2":
        return "historia"
    elif opcao == "3":
        return "ciencias"
    elif opcao == "4":
        return "literatura"
    else:
        print("❌ Escolha uma opção válida!")
        return escolher_area()

#Função para o usuário escolher o nível de dificuldade das perguntas
def nivel_perguntas():
      while True:
        print("Escolha o nível de dificuldade:")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        print()

        opcao = input("Digite o número do nível desejado: ")
        print()

        if opcao == "1":
            return "facil"
        elif opcao == "2":
            return "medio"
        elif opcao == "3":
            return "dificil"
        else:
            print("❌ Opção inválida. Tente novamente.")
            print()
        continue
    

def perguntas(tema, nivel): #função que exibi as perguntas do arquivo JSON
    score = 0
    limite=10
    caminho = f"arquivos/perguntas_{tema}.json" #caminho das perguntas de acordo com o tema

#procura  e carrega o arquivo JSON
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            todas_perguntas = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return 

# Filtra perguntas pelo nível
    perguntas = [p for p in todas_perguntas if p["nivel"] == nivel]
#limitar a quntidade de perguntas

    perguntas=random.sample(perguntas, min(limite,len(perguntas)))

#Exibe as perguntas e opções
    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for letra, texto in pergunta["opcoes"].items():
            print(f"{letra}) {texto}")

        resposta = input("Resposta: ").upper()
        if resposta == pergunta["resposta_correta"]:
            score += 10
            print("🎉 Correto! 🎉")
        else:
            print("🙁 Errado!")
        print()

    return score


#final de jogo e repetição do jogo
def final_jogo(nome):
    while True:
        limpar_terminal()
        tema = escolher_area()
        nivel=nivel_perguntas()
        score = perguntas(tema,nivel)
        print()

        print("Fim de jogo")
        print(f"Pontuação: {score}/100")

        placar(nome, score) #Salva o placar no arquivo json a cada rodada
        ranking()
        print()

        continuar_jogo = input("Jogar novamente? S/N: ").upper()
        if continuar_jogo != "S":
            print("Até a próxima! 👋")
            break


#placar salvo na pasta arquivos
def placar(nome, score):
    novo_placar = {"nome": nome, "pontuação": score}

    # Caminho absoluto da pasta onde está o script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Caminho até a pasta 'arquivos'
    caminho_arquivo = os.path.join(base_dir, "..", "..", "arquivos", "placar.json")

    # Normaliza o caminho para funcionar no Windows e Linux
    caminho_arquivo = os.path.normpath(caminho_arquivo)

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                placares = json.load(arquivo)
        except json.JSONDecodeError:
            placares = []
    else:
        placares = []

    placares.append(novo_placar)

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(placares, arquivo, indent=4, ensure_ascii=False)




#função para mostrar ranking dos jogadores
def ranking():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(base_dir, "..", "..", "arquivos", "placar.json")
    caminho_arquivo = os.path.normpath(caminho_arquivo)

    if not os.path.exists(caminho_arquivo):
        print("Nenhum placar registrado ainda.")
        return

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        placares = json.load(arquivo)

    placares.sort(key=lambda x: x["pontuação"], reverse=True)

    print("\nRANKING DOS JOGADORES 🏆")
    for i, p in enumerate(placares[:3], 1):
        print(i, "-", p["nome"], ":", p["pontuação"])





introducao()
quiz()
