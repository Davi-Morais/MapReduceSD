

def ler_intermediario(intermediario):
    dic_palavras = {}
    with open(intermediario, 'r') as arquivo:
        for line in arquivo.readlines():
            chave, valor = line.strip().split()
            if dic_palavras.get(chave) is not None:
                dic_palavras[chave].append(valor)
            else:
                dic_palavras[chave] = [valor]

# Implementar funcao Reduce

# ler_intermediario('./intermediario')