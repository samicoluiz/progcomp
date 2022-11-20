def somente_numeros(entrada: str) -> bool:
    """Transforma a entrada em uma única linha de caracteres e checa se ela é composta exclusivamente por números"""
    if entrada.replace(" ", "").replace("\n", "").isnumeric():
        return True
    else:
        return False

def vetorizar_entrada(entrada: str) -> list[list[str]]:
    """Transforma cada linha de uma entrada válida em uma lista de números"""
    entrada = entrada.split("\n")
    entrada = [linha.split(" ") for linha in entrada]
    entrada = [[int(elemento) for elemento in linha] for linha in entrada]
    return entrada

def validar(entrada: list[list[int]]) -> bool:
    """Recebe a entrada do usuário e verifica se é válida de acordo com os seguintes requisitos:
    1- A entrada tem pelo menos 3 linhas;
    2- O tamanho da segunda linha é igual ao primeiro elemento da primeira linha;
    3- O numero de linhas restantes após a segunda é igual ao segundo elemento da primeira linha;
    4- Todos os lementos da entrada são números.
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
        print("Entrada válida")
        return True
