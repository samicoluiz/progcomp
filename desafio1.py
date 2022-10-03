#Recebendo o valor de n:
n = int(input('Informe o número de cidades: '))

while n <= 2 or n >= 1500:
    print('Valor inválido.\nO valor precisa estar entre 2 e 1500.')
    continua = int(input("Deseja inserir outro número?"))
    if continua == 1:
        n = int(input('Informe o número de cidades: '))
    else:
        print('Encerrando')
        break
else:
    #Calculando as Combinações 2 a 2:
    matriz = [[], []]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            matriz[0].append([i, j])
    #Pedindo o t de cada cidade:
    for i in matriz[0]:
        matriz[1].append(int(input(f'Insira o tempo entre as cidades {i[0]} e {i[1]}')))
    #Gerador de possibilidades de visitas considerarando a condição k:
    casos = [[x for x in range(1, n+1)]]
    tempos = []
    tempo = 0
    for i in range(len(casos[0])-1):
        try:
            j = matriz[0].index([casos[0][i], casos[0][i+1]])
        except:
            j = matriz[0].index([casos[0][i+1], casos[0][i]])
        tempo += matriz[1][j]
    tempos.append(tempo)

    for i in range(2, n+1):
        for j in range(len(casos)):
            x = casos[j].copy()
            x.remove(i)
            x.insert(0,i)
            #Calculando o menor tempo da nova possiblidade gerada
            tempo = 0
            for i in range(len(x)-1):
                try:
                    j = matriz[0].index([x[i], x[i+1]])
                except:
                    j = matriz[0].index([x[i+1], x[i]])
                tempo += matriz[1][j]
            tempos.append(tempo)
            casos.append(x)
    print(f"O menor tempo possível seria: ", min(tempos))