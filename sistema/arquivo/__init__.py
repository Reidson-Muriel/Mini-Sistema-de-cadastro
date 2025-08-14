from re import split
from sistema import cadastro
from sistema.formatacao.formato import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um Erro na criacao")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def listar(nome):
        try:
            with open(nome, "rt") as arquivo:
                cadastro.lista_principal.clear()
                vazio = True
                escreva = ""
                for linha in arquivo:
                    linha = linha.strip()
                    if linha == "" or ";" not in linha:
                        continue
                    vazio = False
                    nome_pessoa, idade = linha.split(";")
                    cadastro.lista_principal.append((nome_pessoa, int(idade)))
                
        except Exception as erro:
            print(f"Erro ao ler o arquivo {erro}!")
        else:
            cadastro.mostrar("Pessoas Cadastrado")
            if vazio == True:
                escreva="esta vazio"
            if escreva != "":
                aviso(escreva)
            else:   
                cadastro.lista_principal

                
def salvar(nome_arquivo,nome, idade):
    with open(nome_arquivo, "a")as arquivo:
        arquivo.write(f"\n{nome};{idade}\n")
        