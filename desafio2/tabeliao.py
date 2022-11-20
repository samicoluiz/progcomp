def logar(entrada: str) -> None:
    with open("log.txt", "a") as log:
        log.write(entrada)

def clr_log() -> None:
    with open("log.txt", "w") as log:
        log.write("")
