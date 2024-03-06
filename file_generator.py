from random import randint, choices
from os import path, makedirs, listdir, remove


def criar_arquivos(nome_arquivo, split):

    dir_name = "arquivos"
    if not path.exists(dir_name):
        makedirs(dir_name)
    
    for arquivo in listdir(dir_name):
        remove(f'{dir_name}/{arquivo}')
    
    arquivos_criados = []
    for i in range(split):
        novo_arquivo_path = f'./{dir_name}/{nome_arquivo}{i}.txt'
        open(novo_arquivo_path, 'x').close()
        arquivos_criados.append(novo_arquivo_path)
    
    return arquivos_criados 


def gerar_palavras(n, alfabeto, minimo, maximo):
    palavras_geradas = []
    for _ in range(n):
        numero_letras = randint(minimo, maximo)
        
        nova_palavra = "".join(choices(alfabeto, k=numero_letras))

        palavras_geradas.append(nova_palavra)
    return palavras_geradas


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

    arquivos = criar_arquivos(nome_arquivo=nome_arquivo, split=split)

    palavras_geradas = gerar_palavras(n=n, alfabeto=alfabeto, minimo=minimo, maximo=maximo)
    
    splited = [palavras_geradas[i::split] for i in range(split)]

    for i in range(split):
        arq = open(arquivos[i], "w")
        arq.write(" ".join(splited[i]))


    return palavras_geradas


palavras = file_generator(200, "abcd", 2, 4, "arquivo_teste", 10)