from pathlib import Path
from emit import emitir_intermediario, emitir_final

def Map(path_arquivo):
    """Lê um arquivo e emite a ocorrência de uma mesma palavra

    Args:
        path_arquivo (string): caminho do arquivo a ser lido
    """

    arquivo = Path(path_arquivo)
    palavras = arquivo.read_text(encoding="utf-8").split()
    
    for palavra in palavras:
        emitir_intermediario(palavra, '1')


def Reduce(chave, lista_ocorrencia):
    """Recebe e emite uma chave junto da sua acorrencia

    Args:
        chave (string): o nome de uma chave/palavra qualquer
        lista_ocorrencia (string[]): uma lista de ocorrencias dessa chave
    """
    emitir_final(chave, len(lista_ocorrencia))
