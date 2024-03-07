from pathlib import Path
from emit import emitir_intermediario

def Map(path_arquivo):
    """Lê um arquivo e emite a ocorrência de uma mesma palavra

    Args:
        path_arquivo (string): caminho do arquivo a ser lido
    """

    arquivo = Path(path_arquivo)
    palavras = arquivo.read_text(encoding="utf-8").split()
    
    for palavra in palavras:
        emitir_intermediario(palavra, '1')