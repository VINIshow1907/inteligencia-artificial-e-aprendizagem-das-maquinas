from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def identificar_saudacao(mensagem):
    mensagem = mensagem.lower()
    if "bom dia" in mensagem:
        return "Bom dia"
    elif "boa tarde" in mensagem:
        return "Boa tarde"
    elif "boa noite" in mensagem:
        return "Boa noite"
    elif "olá" in mensagem or "oi" in mensagem:
        return "Olá"
    else:
        return "Olá"

mensagem_inicial = input("Você: ")
saudacao = identificar_saudacao(mensagem_inicial)

print(f"ChatBoot: {saudacao}! Qual é o seu nome?")
nome = input("Você: ")

while True:
    print(f"\nChatBoot: O que você deseja, senhor(a) {nome}?")
    print("Digite 1 para falar com o pessoal do escritório")
    print("Digite 2 para assuntos sobre Imposto de Renda")
    print("Digite 3 para assuntos sobre ITR (Imposto Territorial Rural)")
    print("Digite 'sair' para encerrar o atendimento")

    opcao_principal = input("Você: ").strip().lower()

    if opcao_principal == "sair":
        print("ChatBoot: Obrigado pelo contato. Até logo!")
        break

    # Escritório
    elif opcao_principal == "1":
        while True:
            print("\nChatBoot: Com quem você deseja falar?")
            print("Digite 1 para falar com Adriano")
            print("Digite 2 para falar com Fabiana")
            print("Digite 3 para falar com Bruna")
            print("Digite 'voltar' para retornar ao menu anterior")

            opcao = input("Você: ").strip().lower()

            if opcao == "voltar":
                break
            elif opcao == "1":
                print(f"{saudacao} {nome}, vou te passar o número da Adriano: (17) 99999-1111")
            elif opcao == "2":
                print(f"{saudacao} {nome}, vou te passar o número da Fabiana: (17) 99999-2222")
            elif opcao == "3":
                print(f"{saudacao} {nome}, vou te passar o número da Bruna: (17) 99999-3333")
            else:
                print("ChatBoot: Opção inválida.")

    # Imposto de Renda
    elif opcao_principal == "2":
        while True:
            print("\nChatBoot: Escolha uma das opções abaixo:")
            print("Digite 1 para pedir o Imposto de Renda")
            print("Digite 2 para pedir o Darf de Imposto de Renda")
            print("Digite 3 para fazer a Declaração do Imposto de Renda")
            print("Digite 'voltar' para retornar ao menu anterior")

            opcao = input("Você: ").strip().lower()

            if opcao == "voltar":
                break
            elif opcao == "1":
                print(f"{saudacao} {nome}, iremos mandar seu Imposto de Renda no e-mail cadastrado. Muito obrigado!")
            elif opcao == "2":
                print(f"{saudacao} {nome}, iremos mandar o Darf de Imposto no e-mail cadastrado. Muito obrigado!")
            elif opcao == "3":
                print(f"{saudacao} {nome}, iremos fazer sua Declaração de Imposto de Renda. Assim que for concluída, mandaremos no seu e-mail cadastrado. Muito obrigado!")
            else:
                print("ChatBoot: Opção inválida.")

    # ITR
    elif opcao_principal == "3":
        while True:
            print("\nChatBoot: Escolha uma das opções abaixo:")
            print("Digite 1 para pedir o ITR")
            print("Digite 2 para pedir o Darf de ITR")
            print("Digite 3 para fazer o ITR")
            print("Digite 'voltar' para retornar ao menu anterior")

            opcao = input("Você: ").strip().lower()

            if opcao == "voltar":
                break
            elif opcao == "1":
                print(f"{saudacao} {nome}, iremos mandar seu ITR no e-mail cadastrado. Muito obrigado!")
            elif opcao == "2":
                print(f"{saudacao} {nome}, iremos mandar o Darf de ITR no e-mail cadastrado. Muito obrigado!")
            elif opcao == "3":
                print(f"{saudacao} {nome}, iremos fazer seu ITR. Assim que for concluído, mandaremos no seu e-mail cadastrado. Muito obrigado!")
            else:
                print("ChatBoot: Opção inválida.")

    else:
        print("ChatBoot: Opção inválida. Tente novamente.")
