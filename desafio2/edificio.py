from dataclasses import dataclass, field


@dataclass
class Edificio:
    andares: int
    pessoas_por_andar: list[int]
    # pessoas_por_andar: list[int] = field(default_factory = lambda: [0])

    # def __post_init__(self):
    #     self.pessoas_por_andar = [0] * self.andares

    def mudanca(self, andar: int, nova_população: int) -> None:
        """Altera o número de moradores em um andar.
        Recebe o andar e o novo valor de população alterando o atributo pessoas_por_andar correspondente.
        """
        self.pessoas_por_andar[andar-1] = nova_população
    
    def censo(self, andar_limite: int) -> int:
        """Conta todos os moradores residentes no edificio do andar 1 até o andar_limite."""
        return sum(self.pessoas_por_andar[:andar_limite])

    def sindico(self, evento: list[int]) -> int:
        """Aplica o método adequado a entrada segundo a seguinte regra:
        1- Caso a entrada seja uma lista de tamanho 3, aplicar o metodo mudanca
        2- Caso a entrada seja uma lista de tamanho 2, aplicar o metodo censo"""
        if evento[0] == 0:
            self.mudanca(evento[1], evento[2])
        elif evento[0] == 1:
            print(self.censo(evento[1]))

# andares = slice(0, 1)
# populacao = slice(1, 2)