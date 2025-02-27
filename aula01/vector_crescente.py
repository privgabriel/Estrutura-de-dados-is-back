def bubble_sort():
    vector = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    
    for i in range(len(vector)):
        for j in range(len(vector) - 1):
            if vector[j] > vector[j + 1]:
                aux = vector[j]
                vector[j] = vector[j + 1]
                vector[j + 1] = aux
    print(vector)

bubble_sort()