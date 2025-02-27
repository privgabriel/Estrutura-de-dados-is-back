def vectorPar():
    vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(vector)):
        if vector[i] % 2 == 0:
            print(f'vector[{i}] = {vector[i]}')

vectorPar()