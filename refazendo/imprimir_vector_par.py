def imprimir_vector_par():
    vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(vector)):
        if vector[i] % 2 == 0:
            print(f'vector par: {vector[i]}')
        else:
            print(f'vector impar: {vector[i]}')

imprimir_vector_par()