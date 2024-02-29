from pathlib import Path
from os import path

def EmitirIntermediario(chave, ocorrencia):
    """Escreve em um arquivo intermediario um valor chave 
    seguido de sua acorrencia

    Args:
        chave (string): Nome da chave
        ocorrencia (char): o total de ocorrencias
    """

    intermediario = "./intermediario"
    if not path.exists(intermediario):
        open(intermediario, 'w').close()

    with open(intermediario, "a") as arquivo:
        arquivo.write("{} {}\n".format(chave, ocorrencia))


def Map(path_arquivo):
    """Lê um arquivo e emite a ocorrência de uma mesma palavra

    Args:
        path_arquivo (string): caminho do arquivo a ser lido
    """

    arquivo = Path(path_arquivo)
    palavras = arquivo.read_text(encoding="utf-8").split()
    
    for palavra in palavras:
        EmitirIntermediario(palavra, '1')