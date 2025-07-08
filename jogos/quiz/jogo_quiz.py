import json  # Importa o módulo json para trabalhar com arquivos JSON (leitura e escrita de placares/perguntas).
import time  # Importa o módulo time para funções relacionadas a tempo, como pausas (sleep).
import random  # Importa o módulo random para selecionar perguntas aleatoriamente.
import os  # Importa o módulo os para interagir com o sistema operacional, como manipular caminhos de arquivo.
from utils.funcoes import limpar_terminal  # Importa a função 'limpar_terminal' de um módulo utilitário.
import msvcrt  # Biblioteca do Windows para ler teclas uma por uma


def introducao():
    """
    Exibe a tela de introdução e as regras do jogo Quiz.
    Limpa o terminal e aguarda a interação do usuário para iniciar.
    """
    limpar_terminal()  # Limpa a tela do terminal para uma exibição limpa.
    print("=" * 60)  # Imprime uma linha de separação.
    print(" 🎮 BEM-VINDO AO QUIZ 🎮 ".center(60))  # Título centralizado do jogo.
    print("=" * 60)  # Imprime uma linha de separação.

    print("\n✨ REGRAS DO JOGO ✨\n")  # Título das regras.

    print("📖 Escolha uma área de conhecimento:")  # Instrução para escolher a área.
    print("   ➤ Geografia, História, Ciências ou Literatura.\n")  # Opções de áreas.

    print("🎯 Selecione o nível de dificuldade:")  # Instrução para escolher o nível.
    print("   ➤ Fácil, Médio ou Difícil.\n")  # Opções de níveis.

    print("⭐ Cada pergunta vale 10 pontos.")  # Informa a pontuação por pergunta.
    print("   ➤ Responda com a letra correta da opção (A, B, C ou D).\n")  # Instrução de como responder.

    print("⏳ Você terá 15 segundos para responder a cada pergunta.") # Informa sobre o limite de tempo
    print("   ➤ Se o tempo acabar, a pergunta será considerada ERRADA!\n")

    print("🏆 No final, sua pontuação será salva e você verá o ranking dos melhores jogadores!")  # Informa sobre o placar e ranking.
    
    print("\nBoa sorte! Divirta-se! 🍀🎮\n")  # Mensagem de boa sorte.
    input('Pressione ENTER para começar o desafio...')  # Aguarda a entrada do usuário para continuar.


def nome_usuario():
    """
    Solicita e valida o nome (ou apelido) do usuário antes de iniciar o quiz.
    Garante que o nome não seja vazio.
    :return: O nome (string) digitado pelo usuário.
    """
    limpar_terminal()  # Limpa a tela.
    print("=" * 60)  # Linha de separação.
    print(" 📝 SEU NOME, POR FAVOR 📝 ".center(60))  # Título.
    print("=" * 60 + "\n")  # Linha de separação.

    print("Olá, futuro craque do conhecimento!\n")  # Mensagem de boas-vindas.
    print("Para começarmos essa jornada, preciso saber como devo te chamar.\n")  # Explicação da solicitação do nome.

    nome = input("👉 Digite seu nome (ou apelido): ").strip()  # Pede o nome e remove espaços extras.

    while not nome:  # Loop para garantir que o nome não seja vazio.
        print("\nOps! Parece que você não digitou nada. Por favor, insira seu nome para continuar.")
        time.sleep(2)  # Pausa por 2 segundos.
        nome = input("\n👉 Digite seu nome (ou apelido): ").strip()  # Pede o nome novamente.

    print(f"\nMuito bem, {nome}! Vamos ao quiz! 🚀\n")  # Confirma o nome e indica o início do quiz.
    input('Pressione ENTER para iniciar o desafio...')  # Aguarda a entrada do usuário.

    return nome  # Retorna o nome validado.

def escolher_area():
    """
    Permite ao usuário escolher uma área de conhecimento para o quiz.
    Valida a entrada do usuário, garantindo que uma opção válida seja selecionada.
    :return: O nome da área de conhecimento escolhida (string em minúsculas).
    """
    limpar_terminal()  # Limpa a tela.
    print("=" * 60)  # Linha de separação.
    print(" 📚 SELEÇÃO DE CONHECIMENTO 📚 ".center(60))  # Título.
    print("=" * 60 + "\n")  # Linha de separação.

    print("🔍 Escolha a sua área de conhecimento para começar:\n")  # Instrução para escolha.

    print("   1 - Geografia 🌍")  # Opção 1.
    print("   2 - História 🏰")  # Opção 2.
    print("   3 - Ciências 🧪")  # Opção 3.
    print("   4 - Literatura 📖\n")  # Opção 4.

    opcao = input("👉 Digite o NÚMERO da área escolhida: ")  # Solicita a opção ao usuário.
    print()

    # Retorna o nome da área correspondente à opção escolhida.
    if opcao == "1":
        return "geografia"
    elif opcao == "2":
        return "historia"
    elif opcao == "3":
        return "ciencias"
    elif opcao == "4":
        return "literatura"
    else:  # Se a opção for inválida.
        print("❌ Escolha uma opção válida! ")  # Mensagem de erro.
        time.sleep(2.5)  # Pausa para o usuário ler a mensagem.
        return escolher_area()  # Chama a função recursivamente até obter uma entrada válida.

def nivel_perguntas():
    """
    Permite ao usuário escolher o nível de dificuldade das perguntas.
    Valida a entrada do usuário, garantindo que uma opção válida seja selecionada.
    :return: O nível de dificuldade escolhido (string em minúsculas).
    """
    while True:  # Loop para garantir uma entrada válida.
        limpar_terminal()  # Limpa a tela.
        print("=" * 60)  # Linha de separação.
        print(" 🧠 NÍVEL DE DIFICULDADE 🧠 ".center(60))  # Título.
        print("=" * 60 + "\n")  # Linha de separação.

        print("Selecione o desafio que você quer enfrentar:\n")  # Instrução para escolha.

        print("   1 - Fácil 👶")  # Opção 1.
        print("   2 - Médio 🧑‍🎓")  # Opção 2.
        print("   3 - Difícil 🤯\n")  # Opção 3.

        opcao = input("👉 Digite o NÚMERO do nível desejado: ").strip()  # Solicita a opção e remove espaços.
        print()

        # Retorna o nível de dificuldade correspondente à opção.
        if opcao == "1":
            return "facil"
        elif opcao == "2":
            return "medio"
        elif opcao == "3":
            return "dificil"
        else:  # Se a opção for inválida.
            print("❌ Opção inválida. Tente novamente.")  # Mensagem de erro.
            time.sleep(2.5)  # Pausa.
            print()
            continue  # Continua o loop para pedir a entrada novamente.


def limpar_buffer_teclado():
# Enquanto houver teclas "presas" no teclado (ENTER antigo), descarta todas
    while msvcrt.kbhit():     # Enquanto houver tecla pressionada no buffer
        msvcrt.getch()     # Leia e descarte o caractere


def tempo(prompt, timeout):
    print(prompt, end='', flush=True)
    entrada = "" #Inicializa a variável para armazenar o que o usuário digitar
    inicio = time.time() # marca o horário de início da contagem regressiva.

    while True:  # Loop para capturar cada tecla pressionada
        if msvcrt.kbhit():  # Verifica se o usuário pressionou alguma tecla
            char = msvcrt.getwch()   # Lê o caractere digitado
            if char in ('\r', '\n'):  # Enter
                print()
                break
            elif char == '\b':  # Backspace
                entrada = entrada[:-1]
                print('\b \b', end='', flush=True)
            else:
                entrada += char   # Adiciona o caractere digitado à string
                print(char, end='', flush=True)

        if (time.time() - inicio) > timeout: # Verifica se o tempo limite foi ultrapassado
            limpar_buffer_teclado()
            return None   # Retorna None porque o tempo acabou


        time.sleep(0.05) #pausa

    return entrada.strip()




def perguntas(tema, nivel):
    """
    Carrega as perguntas de um arquivo JSON, as filtra por tema e nível,
    apresenta as perguntas ao usuário, gerencia as respostas e calcula a pontuação.

    :param tema: A área de conhecimento das perguntas (string).
    :param nivel: O nível de dificuldade das perguntas (string).
    :return: A pontuação total (int) obtida pelo jogador.
    """
    score = 0  # Inicializa a pontuação do jogador.
    # Constrói o caminho para o arquivo JSON de perguntas baseado no tema.
    caminho = f"arquivos/perguntas_{tema}.json"

    try:
        # Abre e carrega as perguntas do arquivo JSON.
        with open(caminho, "r", encoding="utf-8") as arquivo:
            todas_perguntas = json.load(arquivo)
    except FileNotFoundError:  # Lida com o erro se o arquivo não for encontrado.
        limpar_terminal()
        print("\n" + "=" * 60)
        print(" ERRO: Arquivo de perguntas não encontrado! ".center(60))
        print(f" Verifique se o arquivo '{caminho}' existe.".center(60))
        print("=" * 60)
        time.sleep(3)
        return score  # Retorna a pontuação zero em caso de erro.
    except json.JSONDecodeError:  # Lida com o erro se o JSON for inválido.
        limpar_terminal()
        print("\n" + "=" * 60)
        print(" ERRO: Conteúdo do arquivo de perguntas inválido! ".center(60))
        print(f" O arquivo '{caminho}' não é um JSON válido.".center(60))
        print("=" * 60)
        time.sleep(3)
        return score  # Retorna a pontuação zero em caso de erro.

    # Filtra as perguntas com base no nível selecionado pelo usuário.
    perguntas_filtradas = [p for p in todas_perguntas if p["nivel"].lower() == nivel.lower()]
    
    num_perguntas_a_exibir = 10  # Define o número de perguntas a serem exibidas.
    if len(perguntas_filtradas) >= num_perguntas_a_exibir:
        # Seleciona aleatoriamente o número de perguntas desejado.
        perguntas_para_o_quiz = random.sample(perguntas_filtradas, num_perguntas_a_exibir)
    else:
        # Se houver menos perguntas que o desejado, usa todas as perguntas filtradas.
        perguntas_para_o_quiz = perguntas_filtradas
        # Exibe um aviso se houver menos de 10 perguntas, se necessário
        if len(perguntas_filtradas) > 0:
            print(f"\nAVISO: Apenas {len(perguntas_filtradas)} perguntas disponíveis para este tema/nível. Exibindo todas.")
            time.sleep(2)

    if not perguntas_para_o_quiz:  # Verifica se nenhuma pergunta foi encontrada após a filtragem.
        limpar_terminal()
        print("\n" + "=" * 60)
        print(" Nenhuma pergunta encontrada para este tema/nível! ".center(60))
        print(" Verifique seu arquivo JSON. ".center(60))
        print("=" * 60)
        time.sleep(3)
        return score  # Retorna pontuação zero se não houver perguntas.

    # Loop para iterar sobre cada pergunta selecionada para o quiz.
    for i, pergunta in enumerate(perguntas_para_o_quiz):
        limpar_terminal()  # Limpa a tela antes de cada nova pergunta.

        print("=" * 60)
        print(f" QUIZ - {tema.upper()} ({nivel.upper()}) ".center(60, "="))  # Título do quiz.
        print("=" * 60)

        print(f"\n📚 Pergunta {i + 1}/{len(perguntas_para_o_quiz)}:".center(60))  # Número da pergunta atual.
        print("-" * 60)
        print(f"{pergunta['pergunta']}".center(60))  # Exibe o texto da pergunta.
        print("-" * 60 + "\n")

        # Exibe as opções de resposta para a pergunta.
        for letra, texto in pergunta["opcoes"].items():
            print(f"{letra}) {texto}")

        print("\n" + "=" * 60)
        limpar_buffer_teclado()  # limpa teclas "presas"
        # Solicita a resposta com tempo limite
        resposta = tempo("👉 Sua resposta (digite a letra): ", 15)
      

        if resposta is None:
            print("\n" + "=" * 60)
            print("\n" + "⏰ Tempo limite excedido. Avançando para a próxima pergunta. ". center(60))
            print(f"A resposta correta era: {pergunta['resposta_correta']}) {pergunta['opcoes'][pergunta['resposta_correta']]} ".center(60))
            print("\n" + "=" * 60)
            time.sleep(3.5)
            continue
        else:
            resposta = resposta.upper().strip()

        # Loop para validar a resposta do usuário, garantindo que seja uma opção válida (A, B, C, D).
            while resposta not in pergunta["opcoes"].keys():
                print("\n❌ Resposta inválida! Por favor, digite uma das letras (A, B, C, D).")
                resposta = input("👉 Sua resposta: ").upper().strip()

        # Verifica se a resposta do usuário está correta.
        if resposta == pergunta["resposta_correta"]:
            score += 10  # Adiciona 10 pontos à pontuação se a resposta estiver correta.
            print("\n" + "=" * 60)
            print(" 🎉 CORRETO! Você ganhou 10 pontos! 🎉 ".center(60))  # Mensagem de acerto.
            print("=" * 60)
            time.sleep(2.5)  # Pausa para o usuário ver a mensagem.
        else:
            print("\n" + "=" * 60)
            print(" 🙁 ERRADO! ".center(60))  # Mensagem de erro.
            # Mostra a resposta correta e a opção correspondente.
            print(f"A resposta correta era: {pergunta['resposta_correta']}) {pergunta['opcoes'][pergunta['resposta_correta']]} ".center(60))
            print("\n" + "=" * 60)
            time.sleep(3.5)  # Pausa para o usuário ver a resposta correta.

    return score  # Retorna a pontuação total obtida no quiz.


def quiz():
    """
    Função principal que orquestra o fluxo do jogo Quiz.
    Chama as funções de introdução, escolha de nome, área, nível,
    executa as perguntas e exibe o resultado final, além de gerenciar o placar.
    Permite jogar novamente.
    """
    while True:  # Loop principal do jogo, permite jogar múltiplas vezes.
        limpar_terminal()  # Limpa a tela no início de cada nova partida.
        nome = nome_usuario()  # Obtém o nome do jogador.
        introducao()  # Exibe a introdução e regras.
        tema = escolher_area()  # Permite ao jogador escolher a área.
        nivel = nivel_perguntas()  # Permite ao jogador escolher o nível.
        score = perguntas(tema, nivel)  # Executa o quiz e obtém a pontuação.
        print()

        limpar_terminal()  # Limpa a tela antes de exibir o resultado final.

        print("=" * 60)
        print(" 🏁 FIM DE JOGO! 🏁 ".center(60))  # Título de fim de jogo.
        print("=" * 60 + "\n")

        # Define a mensagem de acordo com a pontuação final.
        if score >= 80:
            msg_score = "Parabéns! Excelente pontuação! 🎉"
        elif score >= 50:
            msg_score = "Bom trabalho! Você se saiu bem! 👍"
        else:
            msg_score = "Continue praticando! Você consegue! 💪"

        print("Sua pontuação final:".center(60))
        print(f" {score}/100 PONTOS ".center(60))  # Exibe a pontuação final.
        print(f"{msg_score}\n".center(60))  # Exibe a mensagem de acordo com a pontuação.

        print("Obrigado por jogar!".center(60))
        print("=" * 60)
        time.sleep(5)  # Pausa para o usuário ver o resultado.

        placar(nome, score)  # Salva a pontuação do jogador no placar.
        ranking()  # Exibe o ranking dos jogadores.
        print()

        # Pergunta ao usuário se deseja jogar novamente.
        continuar_jogo = input("Jogar novamente? S/N: ").upper()
        if continuar_jogo != "S":
            print("Até a próxima! 👋")  # Mensagem de despedida.
            break  # Sai do loop principal, encerrando o jogo.


def placar(nome, score):
    """
    Registra a pontuação do jogador em um arquivo JSON chamado 'placar.json'.
    Cria o arquivo se ele não existir e adiciona novas pontuações.
    Lida com possíveis erros de leitura de JSON.

    :param nome: O nome do jogador (string).
    :param score: A pontuação obtida pelo jogador (int).
    """
    novo_placar = {"nome": nome, "pontuação": score}  # Dicionário com nome e pontuação.

    # Obtém o diretório base do script para garantir que o arquivo 'placar.json' seja salvo no local correto.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(base_dir, "..", "..", "arquivos", "placar.json")

    if os.path.exists(caminho_arquivo):  # Verifica se o arquivo 'placar.json' já existe.
        try:
            # Se existir, lê os placares existentes.
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                placares = json.load(arquivo)
        except json.JSONDecodeError:
            # Se o arquivo existir mas o JSON for inválido, inicia uma lista vazia.
            placares = []
    else:
        # Se o arquivo não existir, inicia uma lista vazia para os placares.
        placares = []

    placares.append(novo_placar)  # Adiciona a nova pontuação à lista de placares.

    # Salva todos os placares (incluindo o novo) de volta no arquivo JSON.
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(placares, arquivo, indent=4, ensure_ascii=False) # 'indent=4' para formatação legível, 'ensure_ascii=False' para caracteres especiais.


def ranking():
    """
    Exibe o ranking dos melhores jogadores com base nas pontuações salvas em 'placar.json'.
    Ordena os jogadores pela pontuação em ordem decrescente e mostra o TOP 3.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(base_dir, "..", "..", "arquivos", "placar.json")

    if not os.path.exists(caminho_arquivo):  # Verifica se o arquivo de placar existe.
        print("Nenhum placar registrado ainda.")  # Mensagem se não houver placar.
        time.sleep(3)
        return

    # Abre e carrega os placares do arquivo JSON.
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        placares = json.load(arquivo)

        # Ordena a lista de placares em ordem decrescente de pontuação.
        # 'lambda x: x["pontuação"]' define a chave de ordenação.
        placares.sort(key=lambda x: x["pontuação"], reverse=True)

    limpar_terminal()  # Limpa a tela antes de exibir o ranking.
    print("=" * 60)
    print(" 🏆 RANKING DOS JOGADORES 🏆 ".center(60))  # Título do ranking.
    print("=" * 60 + "\n")

    print(" TOP 3 MELHORES PONTUAÇÕES ".center(60))

    # Dicionário de emojis para o pódio.
    emojis_podio = {
        1: '🥇',
        2: '🥈',
        3: '🥉'
    }

    # Itera sobre os três primeiros colocados (ou menos, se houver menos que 3).
    for i, p in enumerate(placares[:3], 1):
        nome_jogador = p.get("nome", "Anônimo")  # Obtém o nome do jogador (ou "Anônimo" se não existir).
        pontuacao_jogador = p.get("pontuação", 0)  # Obtém a pontuação (ou 0 se não existir).

        emoji = emojis_podio.get(i, '🏅')  # Pega o emoji correspondente à posição ou um emoji padrão.

        # Formata a string de informação do jogador e a centraliza.
        info_jogador = f"{emoji} {i}º {nome_jogador} ({pontuacao_jogador} PONTOS)"
        print(info_jogador.center(60))
        print("-" * 60)  # Linha divisória.

    print("\nContinue jogando para subir no ranking!".center(60))  # Mensagem de incentivo.
    print("=" * 60)
    time.sleep(5)  # Pausa para o usuário ver o ranking.