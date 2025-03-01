def encontrar_maior_menor_vector():
    vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    maior = vector[0]
    menor = vector[0]

    for i in range(len(vector)):
        if vector[i] > maior:
            maior = vector[i]
        if vector[i] < menor:
            menor = vector[i]
    print(f"O maior elemento do vector é {maior}")
    print(f"O menor elemento do vector é {menor}")

encontrar_maior_menor_vector()