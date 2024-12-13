def exo_1():
    for i in range(1, 11):
        for j in range(i):
            print(i, end=' ')
        print("")

def exo_2():
    value_1 = 214
    value_2 = 86

    #Trouver TOUS les diviseurs communs à la value_1 et value_2
    min_value = min(value_1, value_2)

    for k in range(1, min_value):
        if value_1 % k == 0 and value_2 % k == 0:
            print(k)

def exo_3():
    name = ["A", "B", "C", "D"]
    nbr = [1, 2, 3, 4]

    for l in range(len(nbr)):
        for m in range(len(name)):
            print(f"{nbr[l]} {name[m]}", end = "    |")
        print("\n" + "_" * 50)

def exo_4():
    name = ["A", "B", "C", "D"]
    nbr = [1, 2, 3]

    for n in range(len(nbr)):
        for o in range(len(name)):
            print(f"{nbr[o]} {name[n]}", end = "    |")
        print("\n" + "_" * 50)

    #Génération de la matrice avec les bonnes dimensions
    row = ["-"] * len(name)
    matrix = []
    for i in range(len(nbr)):
        matrix.append(row)
    print(matrix)

    #Remplir la matrice
    for p in range(len(matrix)):
        for q in range(len(matrix[q])):
            matrix[p][q] = f"{nbr[p]} {name[q]}"

    print(matrix)

exo_4()