from matplotlib import pyplot as plt

def get_specs(arquivo: str) -> tuple[int, int, list[int]]:
    """Lê as especificações de um arquivo de texto.
    Recebe:
        arquivo -- o nome de um arquivo contendo as specs
    Retorna:
        n -- numero de divisões no lote
        taxa -- valor da taxa aplicada
        terrenos -- lista com as areas dos terrenos do lote
    """
    with open(arquivo, "r") as f:
        entrada = f.read().split("\n")
    primeira_linha = entrada[0].split()
    n, taxa = int(primeira_linha[0]), float(primeira_linha[1])
    lote = [int(i) for i in entrada[1].split()]
    return n, taxa, lote

def anterior(lote: list, terreno: int) -> int:
    """Recebe um indice e retorna o indice anterior considerando
    que as extremidades da lista são vizinhas
    """
    vizinho_anterior = ((terreno-1) % len(lote))
    return vizinho_anterior

def seguinte(lote: list, terreno: int) -> int:
    """Recebe um indice e retorna o indice seguinte considerando
    que as extremidades da lista são vizinhas
    """
    vizinho_seguinte = ((terreno+1) % len(lote))
    return vizinho_seguinte

def terreno_alvo(lote: list[int]) -> int:
    """Identifica o melhor terreno para realiza uma união
    Recebe:
        lote -- uma lista com as areas dos terrenos
    Retorna:
        valor_alvo -- o indice do terreno alvo no lote
    """
    # Considerando os pares de vizinhos do lote, encontra o menor valor entre
    # os elementos de maior valor presentes dos pares
    numero, valor_alvo = min((max(lote[anterior(lote, i)], lote[i]), i) for i in range(len(lote)))
    if numero == lote[valor_alvo]:
        return valor_alvo
    else:
        valor_alvo = anterior(lote, valor_alvo)
        return valor_alvo
    
def vizinho_alvo(lote: list[int], terreno_alvo: int) -> int:
    """Identifica o melhor vizinho do terreno_alvo para realizar uma união.
    Recebe:
        lote -- uma lista com as áreas dos terrenos
        terreno_alvo -- o indice do terreno_alvo
    Retorna:
        vizinho_alvo -- o vizinho de menor area para realizar uma união
    """
    menor_vizinho = min(lote[anterior(lote, terreno_alvo)], lote[seguinte(lote, terreno_alvo)])
    if menor_vizinho == lote[anterior(lote, terreno_alvo)]:
        vizinho_alvo = anterior(lote, terreno_alvo)
    else:
        vizinho_alvo = seguinte(lote, terreno_alvo)
    return vizinho_alvo

def taxar(taxa: float, area_terreno: int) -> float:
    """Calcula a taxa incidente sobre o terreno_alvo"""
    valor = taxa * area_terreno
    return valor

def unir_terrenos(lote: list[int], alvo: int, vizinho: int) -> None:
    """Une o terreno alvo e o melhor vizinho na posição de menor indice entre os dois."""
    menor_indice = min(alvo, vizinho)
    if len(lote) > 2:
        lote[menor_indice] += (lote.pop(vizinho) if vizinho > menor_indice else lote.pop(alvo))
    else:
        lote[0] += lote.pop(1)

def desenha_lote(lote: list[int]) -> None:
    """Gera um gráfico de rosca representando o lote (alterar cores de acordo)"""
    plt.pie(lote, colors=['#8fbcbb'],labels=lote, labeldistance=.795, wedgeprops = { 'linewidth' : 7, 'edgecolor' : '#2e3440' })
    circulo = plt.Circle((0,0), 0.7, color='#2e3440', label=["LAGO"])
    p = plt.gcf()
    p.gca().add_artist(circulo)
    plt.show()

def resolver_desafio(entrada: str) -> float:
    """Calcula o menor valor possível para as taxas do loteamento
    de acordo com as specs do desafio
    """
    n, taxa, lote = get_specs(entrada)
    taxas_totais = 0
    # print(lote)
    while len(lote) > 1:
        desenha_lote(lote)
        alvo = terreno_alvo(lote)
        taxas_totais += taxar(taxa, lote[alvo])
        vizinho = vizinho_alvo(lote, alvo)
        unir_terrenos(lote, alvo, vizinho)
        # print(f'Taxação parcial: {taxas_totais}')
        # print(lote)
    desenha_lote(lote)
    print(taxas_totais)
    return taxas_totais

#################################################################

resolver_desafio('entrada_2_7.txt')