def somente_numeros(entrada: str) -> bool:
    """Transforma a entrada em uma única linha de caracteres e checa se ela é composta exclusivamente por números"""

    if entrada.replace(" ", "").replace("\n", "").isnumeric():
        return True
    else:
        return False


def vetorizar_entrada(entrada: str) -> list[list[int]]:
    """Transforma cada linha de uma entrada válida em uma lista de números"""

    entrada = entrada.split("\n")
    entrada = [linha.split(" ") for linha in entrada]
    entrada = [[int(elemento) for elemento in linha] for linha in entrada]
    return entrada


def checa_parametros(entrada: list[list[int]]) -> bool:
    """Verifica os requisitos padrão para os parâmetros (as duas primeiras linhas) fornecidos nas especificações.
    São eles:
    1- O primeiro número (N) da primeira linha está no intervalo 1 ≤ N ≤ 10e5
    2- O segundo número (Q) da primeira linha está no intervalo 1 ≤ Q ≤ N
    3- O número de pessoas (Ai) em um determinado andar tem de estar no intervalo 0 ≤ Ai ≤ 1000
    """

    if not 1 <= entrada[0][0] <= 10e5:
        print("O prédio não pode ter mais do que 10e5 andares")
        return False
    elif not 1 <= entrada[0][1] <= entrada[0][0]:
        print("O numero de eventos não pode ser maior do que o numero de andares")
        return False
    elif any(elemento > 1000 for elemento in entrada[1]):
        print("O número de moradores em um andar não pode ser maior do que 1000")
        return False
    else:
        return True


def checa_eventos(entrada: list[list[int]]) -> bool:
    """Verifica os requisitos padrão para os eventos (linhas após a segunda) fornecidos nas especificações. São eles:
    1- Há pelo menos um evento que comece com o número 1
    2- Um determinado andar (K) tem de estar no intervalo 1 ≤ K ≤ N
    3- O número de pessoas (P) que podem se mudar para um determinado andar tem de estar no intervalo 0 <= P <= 1000
    """

    ini_1_counter = 0
    for linha in entrada:
        if linha[0] == 1:
            ini_1_counter += 1

        if not 1 <= linha[1] <= entrada[0][0]:
            print("O numero de unidade é maior do que o tamanho do prédio")
            return False

        if linha[0] == 0 and linha[2] > 1000:
            print("O número de pessoas que vão se mudar não pode ser maior do que 1000")
            return False

    if ini_1_counter > 0:
        return True
    else:
        return False


def checa_forma(entrada: list[list[int]]) -> bool:
    """Recebe a entrada do usuário e verifica se é válida conforme os seguintes requisitos:
    1- A entrada tem pelo menos 3 linhas;
    2- O tamanho da segunda linha é igual ao primeiro elemento da primeira linha;
    3- O número de linhas restantes após a segunda é igual ao segundo elemento da primeira linha;
    4- Todos os elementos da entrada são números.
    """

    if len(entrada) < 3:
        print("Pelo menos 3 parâmetros precisam ser fornecidos na entrada")
        return False

    elif len(entrada[1]) != entrada[0][0]:
        print(f"O número de apartamentos é diferente do especificado ({len(entrada[1])} != {entrada[0][0]})")
        return False
    elif len(entrada[2:]) != entrada[0][1]:
        print(f"O número de eventos é diferente do especificado ({len(entrada[2:])} != {entrada[0][1]})")
        return False
    else:
        return True


def validar(entrada: str) -> bool:
    """Executa as validações uma a uma. Interrompe o código caso encontre algum problema"""

    if somente_numeros(entrada):
        entrada = vetorizar_entrada(entrada)
    else:
        return False
    if checa_forma(entrada):
        if checa_parametros(entrada):
            if checa_eventos(entrada):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
