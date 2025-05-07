while True:
    print("************************************************************")
    print("               CÁLCULO DE GRANDEZAS ELÉTRICAS               ")
    print("************************************************************")
    print("1 - Tensão (em Volt)")
    print("2 - Resistência (em Ohm)")
    print("3 - Corrente (em Ampére)")
    print("0 - Sair")
    print("************************************************************")

    escolha = input("Qual grandeza deseja calcular? (1/2/3 ou 0 para sair): ")

    if escolha == "0":
        print("Programa finalizado!")
        break

    elif escolha == "1":
        try:
            r = float(input("Informe a resistência (Ohm): "))
            i = float(input("Informe a corrente (Ampére): "))
            u = r * i
            print(f"Tensão calculada: {u:.2f} V\n")
        except ValueError:
            print("Entrada inválida. Digite apenas números.\n")

    elif escolha == "2":
        try:
            u = float(input("Informe a tensão (Volt): "))
            i = float(input("Informe a corrente (Ampére): "))
            if i != 0:
                r = u / i
                print(f"Resistência calculada: {r:.2f} Ω\n")
            else:
                print("Erro: a corrente não pode ser zero.\n")
        except ValueError:
            print("Entrada inválida. Digite apenas números.\n")

    elif escolha == "3":
        try:
            u = float(input("Informe a tensão (Volt): "))
            r = float(input("Informe a resistência (Ohm): "))
            if r != 0:
                i = u / r
                print(f"Corrente calculada: {i:.2f} A\n")
            else:
                print("Erro: a resistência não pode ser zero.\n")
        except ValueError:
            print("Entrada inválida. Digite apenas números.\n")

    else:
        print("Opção inválida. Por favor, escolha 1, 2, 3 ou 0 para sair.\n")
