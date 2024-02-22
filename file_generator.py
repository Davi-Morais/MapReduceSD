from random import randint
from os import path

def criar_arquivos(nome_arquivo, split):
    arquivos = []
    for i in range(split):
        nome = "{}{}.txt".format(nome_arquivo, i)
        if not path.exists(nome):
            open(nome, "x").close()
            arquivos.append(nome)
        else:
            arquivos.append(nome)
    return arquivos


def file_generator(n, alfabeto, minimo, maximo, nome_arquivo, split):
    """Gera n palavras aleatorias que podem possuir qualquer tamanho
    entre um minimo e um maximo. Gera um arquivo com essas palavras

    Args:
        n (int): numero de palavras geradas.
        alfabeto (string): uma string com as letras que devem ser usadas para gerar as palavras.
        minimo (int): tamanho minimo que uma palavra pode ter
        maximo (int): tamanho maximo que uma palavra pode ter
        nome_arquivo (string): nome do arquivo
        split (int): divisao
    """



    tamanho_alfabeto = len(alfabeto)-1

    arquivos = criar_arquivos(nome_arquivo=nome_arquivo, split=split)


    palavras_geradas = []
    for _ in range(n):
        numero_letras = randint(minimo, maximo)
        
        nova_palavra = "".join([ alfabeto[randint(0, tamanho_alfabeto)] for _ in range(numero_letras)])

        palavras_geradas.append(nova_palavra)
    

    
    splited = [palavras_geradas[i::split] for i in range(split)]

    for i in range(split):
        arq = open(arquivos[i], "w")
        arq.write(" ".join(splited[i]))


    return palavras_geradas


palavras = file_generator(200, "abcd", 2, 4, "arquivo_teste", 10)