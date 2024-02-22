from random import randint

def file_generator(n, alfabeto, minimo, maximo, split):
    """Gera n palavras aleatorias que podem possuir qualquer tamanho
    entre um minimo e um maximo. As palavras geradas devem ser divididas(split)
    em conjuntos que serão escritos em arquivos diferentes.

    Args:
        n (int): numero de palavras geradas.
        alfabeto (string): uma string com as letras que devem ser usadas para gerar as palavras.
        minimo (int): tamanho minimo que uma palavra pode ter
        maximo (int): tamanho maximo que uma palavra pode ter
        split (int): quantidade de arquivos que devem ser gerados
    """


    palavras_geradas = []


    for _ in range(n):
        numero_letras = randint(minimo, maximo)
        
        nova_palavra = "".join([alfabeto[randint(0, len(alfabeto)-1)] for _ in range(numero_letras)])

        palavras_geradas.append(nova_palavra)
    

    return palavras_geradas


# palavras = file_generator(20, "abcdef", 2, 6, 10)
# print(palavras)