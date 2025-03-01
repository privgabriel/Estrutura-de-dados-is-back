def ordenar_vector():
    vector = [45, 23, 67, 12, 89, 34, 23, 90, 56, 78]
    
    for i in range(len(vector)):
        for j in range(i+1, len(vector)):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]
    print(vector)

ordenar_vector()