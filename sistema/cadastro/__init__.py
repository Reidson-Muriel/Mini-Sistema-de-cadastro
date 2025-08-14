from sistema.formatacao.formato import *
from sistema.arquivo import *

lista_principal = list()

def mostrar(txt):
    res = sorted(lista_principal, key=lambda x:x[0].lower())
    formatar(txt)
    for nome, idade in res:
        print(f"{(nome).ljust(20)} {str(idade).rjust(3)} anos\n",end="")
    


def novo_cadastro(nome, idade):
     dupla = (nome, idade)
     lista_principal.append(dupla)

