from input_validation import validar, somente_numeros, vetorizar_entrada
from edificio import Edificio


with open("desafio2/entrada.txt", "r") as f:
    entrada = f.read()

# Validando a entrada    
if somente_numeros(entrada):
    entrada = vetorizar_entrada(entrada)
    if validar(entrada):
        # Instanciando o arranha-céu
        andares, populacao = entrada[0][0], entrada[1]
        arranha_ceu = Edificio(andares, populacao)
        # Executando os eventos
        for evento in entrada[2:]:
            arranha_ceu.sindico(evento)