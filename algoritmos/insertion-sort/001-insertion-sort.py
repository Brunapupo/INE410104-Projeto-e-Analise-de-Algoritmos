a_original = [31, 41, 59, 26, 41, 58]

while True:
    escolha = input(
        "\nDigite 'c' para ordem crescente, 'd' para decrescente ou 'q' para sair: "
    )

    if escolha == "c":
        a = a_original.copy()
        print("\nOrdem crescente")
        for j in range(1, len(a)):
            chave = a[j]
            i = j - 1
            while i >= 0 and a[i] > chave:
                a[i + 1] = a[i]
                i -= 1
            a[i + 1] = chave
            print(f"Interação {j}: {a}")

    elif escolha == "d":
        a = a_original.copy()
        print("\nOrdem decrescente")
        for j in range(1, len(a)):
            chave = a[j]
            i = j - 1
            while i >= 0 and a[i] < chave:
                a[i + 1] = a[i]
                i -= 1
            a[i + 1] = chave
            print(f"Interação {j}: {a}")

    elif escolha == "q":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Digite 'c', 'd' ou 'q'.")
