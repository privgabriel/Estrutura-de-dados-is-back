def vector_menor_maior():
    vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    menor_numero = vector[0]
    maior_numero = vector[0]

    for i in range(len(vector)):
        if vector[i] < menor_numero:
            menor_numero = vector[i]
        if vector[i] > maior_numero:
            maior_numero = vector[i]
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")

vector_menor_maior()

