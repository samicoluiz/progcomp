import pandas as pd
import glob


def create_serie_temporal(metrica: str) -> pd.DataFrame:
    """Recebe a sigla de uma das métricas utilizadas e combina
    todos os arquivos relacionados para montar uma série temporal
    """

    def normalizar_2010_2011() -> None:
        # Aparentemente para os anos de 2010 e 2011 a coluna dos índices segue uma convenção diferente para os nomes,
        # o código abaixo normaliza estes nomes segundo o padrão observado nos dataframes para os anos posteriores.
        for i in dados[:2]:
            i["COL1"] = i["COL1"].str.replace("org.springframework.", "spring-", regex=False)

    dados = []
    # Modificar o caminho de acordo
    caminho = r"D:\OneDrive\Documentos\ciencia_da_computacao\segundo_semestre\programacao_de_computadores\desafio_pandas2\spring-framework\\"
    nome_arquivo = f"{metrica}*.csv"
    for csv in glob.iglob(caminho + nome_arquivo):
        temp_df = pd.read_csv(csv)
        dados.append(temp_df)

    normalizar_2010_2011()  # Comentar esta linha caso esse passo seja desnecessário

    serie_temporal_metrica = pd.concat(dados)
    serie_temporal_metrica = serie_temporal_metrica.groupby(serie_temporal_metrica["COL1"]).sum()
    return serie_temporal_metrica


siglas = ["CBO", "LCO", "LOC", "WMC"]
solucao = [create_serie_temporal(metrica) for metrica in siglas]
