def logar(entrada: str) -> None:
    """Loga as entradas executadas no desafio"""
    with open("desafio2/log.txt", "a") as log:
        log.write(f"{entrada}\n{'-' * 30}\n")

def clr_log() -> None:
    """Limpa o log"""
    with open("desafio2/log.txt", "w") as log:
        log.write("")