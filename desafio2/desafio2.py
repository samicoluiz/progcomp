from input_validation import validar, somente_numeros, vetorizar_entrada
from edificio import Edificio
from tabeliao import logar, clr_log


with open("desafio2/entrada.txt", "r") as f:
    entrada = f.read()

# Validando a entrada    
if somente_numeros(entrada):
    entrada_num = vetorizar_entrada(entrada)
    if validar(entrada_num):
        # Instanciando o arranha-céu
        andares, populacao = entrada[0][0], entrada[1]
        
        arranha_ceu = Edificio(andares, populacao)
        # Executando os eventos
        for evento in entrada[2:]:
            arranha_ceu.sindico(evento)