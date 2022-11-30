from dataclasses import dataclass
from matplotlib import pyplot as plt


@dataclass
class Edificio:
    andares: int
    pessoas_por_andar: list[int]

    def mudanca(self, andar: int, nova_populacao: int, desenhar: bool = False) -> None:
        """Altera o número de moradores em um andar.
        Recebe o andar e o novo valor de população alterando o atributo pessoas_por_andar correspondente.
        """

        def desenhar_mudanca():
            fig, ax = plt.subplots()
            andares = range(len(self.pessoas_por_andar))
            bottom = 0
            labels = [str(i) for i in self.pessoas_por_andar]
            for piso in andares:
                cor = ("#8fbcbb" if piso != andar - 1 else "#ebcb8b")
                x = 1
                y = 1
                p = ax.bar(x, y, bottom=bottom, width=.35, label=labels[piso], color=cor, edgecolor="#81a1c1")
                ax.bar_label(p, label_type='center', labels=[labels[piso]])
                ax.set_xticks(list(range(3)))
                bottom += y
            plt.tick_params(
                axis='x',  # changes apply to the x-axis
                which='both',  # both major and minor ticks are affected
                bottom=False,  # ticks along the bottom edge are off
                top=False,  # ticks along the top edge are off
                labelbottom=False)  # labels along the bottom edge are off
            plt.title("Mudança")
            # ax.set_facecolor("#e5e9f0")
            # fig.set_facecolor("#eceff4")
            # plt.savefig('figs/my_plot.png')
            plt.show()

        self.pessoas_por_andar[andar - 1] = nova_populacao
        if desenhar is True:
            desenhar_mudanca()

    def censo(self, andar_limite: int, desenhar: bool = False) -> int:
        """Conta todos os moradores residentes no edificio do andar 1 até o andar_limite."""

        def desenhar_censo():
            fig, ax = plt.subplots()
            pops = [contagem] + self.pessoas_por_andar[andar_limite:]
            pops_indice = range(len(pops))
            bottom = 0
            labels = [str(i) for i in pops]
            for andar in pops_indice:
                cor = ("#8fbcbb" if andar != 0 else "#5e81ac")
                x = 1
                y = (1 if andar > 0 else andar_limite)
                p = ax.bar(x, y, bottom=bottom, width=.35, label=labels[andar], color=cor, edgecolor="#81a1c1")

                ax.bar_label(p, label_type='center', labels=[labels[andar]])
                ax.set_xticks(list(range(3)))
                bottom += y
            # ax.set_facecolor("#eceff4")
            # fig.set_facecolor("#eceff4")
            plt.title("Censo")
            plt.tick_params(
                axis='x',  # changes apply to the x-axis
                which='both',  # both major and minor ticks are affected
                bottom=False,  # ticks along the bottom edge are off
                top=False,  # ticks along the top edge are off
                labelbottom=False)  # labels along the bottom edge are off
            plt.show()

        contagem = sum(self.pessoas_por_andar[:andar_limite])
        if desenhar is True:
            desenhar_censo()
        return contagem

    def sindico(self, evento: list[int]) -> None:
        """Aplica o método adequado a entrada segundo a seguinte regra:
        1- Caso a entrada seja uma lista de tamanho 3, aplicar o método mudanca
        2- Caso a entrada seja uma lista de tamanho 2, aplicar o método censo"""

        if evento[0] == 0:
            self.mudanca(evento[1], evento[2], desenhar=True)
        elif evento[0] == 1:
            print(self.censo(evento[1], desenhar=True))
