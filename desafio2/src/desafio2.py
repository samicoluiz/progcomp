from edificio import Edificio
from input_validation import validar, vetorizar_entrada
from tabeliao import logar

with open("entrada.txt", "r") as f:
    entrada = f.read()

# Validando a entrada
if validar(entrada):
    logar(entrada)
    # Transformar a entrada de uma única str para uma list[int]
    entrada = vetorizar_entrada(entrada)
    # Criando o arranha-céu
    andares, populacao = entrada[0][0], entrada[1]
    arranha_ceu = Edificio(andares, populacao)
    # Executando os eventos
    for evento in entrada[2:]:
        arranha_ceu.sindico(evento)
else:
    print("Entrada inválida")
