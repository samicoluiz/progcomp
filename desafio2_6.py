import numpy as np


# Linhas L
# Colunas C
# Índice começa no 1
# Numeração das cadeiras: (i-1) * C + j
# Mudanças: sempre duas, ou duas linhas, ou duas colunas, uma troca de lugar com a outra
# É preciso fazer o sort em uma linha, através da manipulação das colunas, depois se organiza a ordem das linhas


def check_sorted(vetor: np.array) -> bool:
    return np.array_equal(vetor, np.sort(vetor))


def array_canonico(l: int, c: int) -> np.array:
    array_teste = np.reshape(np.array(np.arange(total_de_numeros)), (l, c))
    return array_teste


def intercambiar_colunas(vetor: np.array, coluna1: int, coluna2: int) -> np.array:
    vetor[:, [coluna1, coluna2]] = vetor[:, [coluna2, coluna1]]
    return vetor


def intercambiar_linhas(vetor: np.array, linha1: np.array, linha2: np.array) -> np.array:
    vetor[[linha1, linha2], :] = vetor[[linha2, linha1], :]
    return vetor


def organizar_linhas(vetor: np.array):
    for i in range(len(vetor)):
        if not check_sorted(vetor[i]):
            primeiro = min(vetor[i])
            for j in range(len(vetor[i])):
                if vetor[i][j] != j + primeiro:
                    numero_correto = np.where(vetor[i] == j + primeiro)[0][0]
                    print(vetor[i])
                    print(f"index = {j}")
                    print(f"valor esperado = {j+primeiro}")
                    print(f"valor encontrado = {vetor[i][j]}")
                    print(f"valor esperado está no index: {numero_correto}")
                    print(f"Intercambiando o elemento no index {j} pelo elemento no index {numero_correto}")
                    intercambiar_colunas(vetor, j, np.where(vetor[i] == j + primeiro)[0][0])
        else:
            print("ordenado")
    return vetor


def organizar_colunas(vetor: np.array):
    vetor = vetor.T
    for i in range(len(vetor)):
        if not check_sorted(vetor[i]):
            primeiro = min(vetor[i])
            for j in range(len(vetor[i])):
                if vetor[i][j] != j * len(vetor[i]):
                    numero_correto = np.where(vetor[i] == j * len(vetor[i])[0][0])
                    print(vetor[i])
                    print(f"index = {j}")
                    print(f"valor esperado = {j+primeiro}")
                    print(f"valor encontrado = {vetor[i][j]}")
                    print(f"valor esperado está no index: {numero_correto}")
                    print(f"Intercambiando o elemento no index {j} pelo elemento no index {numero_correto}")
                    intercambiar_linhas(vetor, j, np.where(vetor[i] == j + primeiro)[0][0])
        else:
            print("ordenado")
    return vetor.T


linhas = 3
colunas = 4
total_de_numeros = linhas * colunas
exemplo_teste = array_canonico(linhas, colunas)
intercambiar_colunas(exemplo_teste, 0, 1)
intercambiar_linhas(exemplo_teste, 0, 1)

print(exemplo_teste)
organizar_linhas(exemplo_teste)
print(organizar_colunas(exemplo_teste))
print(exemplo_teste.T)
print(exemplo_teste)
