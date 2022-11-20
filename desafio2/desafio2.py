from input_validation import validar, somente_numeros, vetorizar_entrada
from edificio import Edificio
from tabeliao import logar, clr_log


with open("desafio2/entrada.txt", "r") as f:
    entrada = f.read()

# Validando a entrada
if validar(entrada):
    logar(entrada)
    entrada = vetorizar_entrada(entrada)
    andares, populacao = entrada[0][0], entrada[1]
    # Criando o arranha-céu
    arranha_ceu = Edificio(andares, populacao)
    print(arranha_ceu)
    # Executando os eventos
    for evento in entrada[2:]:
        arranha_ceu.sindico(evento)