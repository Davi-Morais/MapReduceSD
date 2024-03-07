from os import path


def emitir_intermediario(chave, ocorrencia):
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


def ler_intermediario(intermediario):
    dic_palavras = {}
    with open(intermediario, 'r') as arquivo:
        for line in arquivo.readlines():
            chave, valor = line.strip().split()
            if dic_palavras.get(chave) is not None:
                dic_palavras[chave].append(valor)
            else:
                dic_palavras[chave] = [valor]


def emitir_final(chave, ocorrencia):
    pass
