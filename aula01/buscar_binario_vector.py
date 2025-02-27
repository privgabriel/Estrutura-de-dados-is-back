#Buscar um elemento no vetor (Busca simples e binária)

def busca_simples():
    vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    elemento = int(input("Digite o elemento que deseja buscar: "))

    for i in range(len(vector)):
        if vector[i] == elemento:
            print(f"Elemento encontrado na posição {i}")
            break
    else:
        print("Elemento não encontrado")

def busca_binaria():
    vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    elemento = int(input("Digite o elemento que deseja buscar: "))

    inicio = 0
    fim = len(vector) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vector[meio] == elemento:
            print(f"Elemento encontrado na posição {meio}")
            break
        elif vector[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    else:
        print("Elemento não encontrado")

busca_simples()
busca_binaria()

