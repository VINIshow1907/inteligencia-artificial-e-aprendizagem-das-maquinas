# Importa a função 'pipeline' da biblioteca transformers da Hugging Face
from transformers import pipeline

# Cria uma pipeline de classificação de texto com o modelo pré-treinado específico para sentimento
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Função para identificar uma saudação na mensagem do usuário
def identificar_saudacao(mensagem):
    mensagem = mensagem.lower()  # Converte a mensagem para minúsculas para facilitar a comparação
    if "bom dia" in mensagem:
        return "Bom dia"
    elif "boa tarde" in mensagem:
        return "Boa tarde"
    elif "boa noite" in mensagem:
        return "Boa noite"
    elif "olá" in mensagem or "oi" in mensagem:
        return "Olá"
    else:
        return "Olá"  # Saudação padrão caso nenhuma das anteriores seja identificada

# Solicita uma mensagem inicial do usuário
mensagem_inicial = input("Você: ")

# Chama a função para identificar a saudação apropriada com base na mensagem do usuário
saudacao = identificar_saudacao(mensagem_inicial)

# Exibe a saudação personalizada e pergunta o nome do usuário
print(f"ChatBoot: {saudacao}! Qual é o seu nome?")
nome = input("Você: ")

# Início do loop principal de interação com o chatbot
while True:
    # Menu principal com as opções de atendimento
    print(f"\nChatBoot: O que você deseja, senhor(a) {nome}?")
    print("Digite 1 para falar com o pessoal do escritório")
    print("Digite 2 para assuntos sobre Imposto de Renda")
    print("Digite 3 para assuntos sobre ITR (Imposto Territorial Rural)")
    print("Digite 'sair' para encerrar o atendimento")

    # Recebe a escolha do usuário e normaliza para minúsculas e sem espaços
    opcao_principal = input("Você: ").strip().lower()

    # Caso o usuário digite 'sair', o chatbot encerra a conversa
    if opcao_principal == "sair":
        print("ChatBoot: Obrigado pelo contato. Até logo!")
        break

    # Opção 1 - Escritório
    elif opcao_principal == "1":
        while True:
            print("\nChatBoot: Com quem você deseja falar?")
            print("Digite 1 para falar com Adriano")
            print("Digite 2 para falar com Fabiana")
            print("Digite 3 para falar com Bruna")
            print("Digite 'voltar' para retornar ao menu anterior")

            opcao = input("Você: ").strip().lower()

            if opcao == "voltar":
                break  # Retorna ao menu principal

            elif opcao == "1":
                print(f"{saudacao} {nome}, vou te passar o número da Adriano: (17) 99999-1111")
            elif opcao == "2":
                print(f"{saudacao} {nome}, vou te passar o número da Fabiana: (17) 99999-2222")
            elif opcao == "3":
                print(f"{saudacao} {nome}, vou te passar o número da Bruna: (17) 99999-3333")
            else:
                print("ChatBoot: Opção inválida.")

    # Opção 2 - Imposto de Renda
    elif opcao_principal == "2":
        while True:
            print("\nChatBoot: Escolha uma das opções abaixo:")
            print("Digite 1 para pedir o Imposto de Renda")
            print("Digite 2 para pedir o Darf de Imposto de Renda")
            print("Digite 3 para fazer a Declaração do Imposto de Renda")
            print("Digite 'voltar' para retornar ao menu anterior")

            opcao = input("Você: ").strip().lower()

            if opcao == "voltar":
                break  # Retorna ao menu principal

            elif opcao == "1":
                print(f"{saudacao} {nome}, iremos mandar seu Imposto de Renda no e-mail cadastrado. Muito obrigado!")
            elif opcao == "2":
                print(f"{saudacao} {nome}, iremos mandar o Darf de Imposto no e-mail cadastrado. Muito obrigado!")
            elif opcao == "3":
                print(f"{saudacao} {nome}, iremos fazer sua Declaração de Imposto de Renda. Assim que for concluída, mandaremos no seu e-mail cadastrado. Muito obrigado!")
            else:
                print("ChatBoot: Opção inválida.")

    # Opção 3 - ITR (Imposto Territorial Rural)
    elif opcao_principal == "3":
        while True:
            print("\nChatBoot: Escolha uma das opções abaixo:")
            print("Digite 1 para pedir o ITR")
            print("Digite 2 para pedir o Darf de ITR")
            print("Digite 3 para fazer o ITR")
            print("Digite 'voltar' para retornar ao menu anterior")

            opcao = input("Você: ").strip().lower()

            if opcao == "voltar":
                break  # Retorna ao menu principal

            elif opcao == "1":
                print(f"{saudacao} {nome}, iremos mandar seu ITR no e-mail cadastrado. Muito obrigado!")
            elif opcao == "2":
                print(f"{saudacao} {nome}, iremos mandar o Darf de ITR no e-mail cadastrado. Muito obrigado!")
            elif opcao == "3":
                print(f"{saudacao} {nome}, iremos fazer seu ITR. Assim que for concluído, mandaremos no seu e-mail cadastrado. Muito obrigado!")
            else:
                print("ChatBoot: Opção inválida.")

    # Caso o usuário digite uma opção que não existe
    else:
        print("ChatBoot: Opção inválida. Tente novamente.")