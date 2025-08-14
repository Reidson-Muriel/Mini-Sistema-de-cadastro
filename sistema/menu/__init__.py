from sistema import cadastro
from sistema.cadastro import novo_cadastro
from sistema import arquivo

arq = "Curso.txt"
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

def menu():
    while True:
        print("-"*30)
        print("Menu Principal".center(30))
        print("-"*30)
        print("\033[33m1 \033[0m- \033[34mMostrar pessoas cadastradas\033[0m" \
        "\n\033[33m2 \033[0m- \033[34mCadastrar novo\033[0m" \
        "\n\033[33m3 \033[0m- \033[31msair\033[0m")
        print("-"*30)
        try:
            op = input("Digite a opcao>> ")
            opcao = int(op)
        except ValueError:
            print("Erro, digite somente o numero")
            continue
        except KeyboardInterrupt:
            print(f"usuario preferiu nao colocar nessa opcao {opcao}")
            break
            

        if opcao == 1:
            arquivo.listar(arq)
        elif opcao == 2:
            nom = input("digite o nome: ")
            while True:
                age = input("Digite a idade: ")
                try:
                    idad = int(age)
                    arquivo.salvar(arq, nom, idad)
                    cadastro.novo_cadastro(nom, idad)
                    print("Adicionado com sucesso!")
                    break
                except ValueError:
                    print("Erro, somente em numero!")
        elif opcao == 3:
            print("Encerrado com sucesso!")
            break
        else:
            print("nao temos esse opcao!")

