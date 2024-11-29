from cadastro import *   #para importar informações de outro arquivo (From arquivo import) * é tudo que tem na pasta


while True:
    op = int(input("Bem vindo\n Para fazer cadastro escolha a opção desejada:\n1-Pessoa Física\n2-Pessoa Jurídica"))
    if op == 1:
        instancia=PFisica()
        instancia.PF()
    elif op == 2:
        instancia=PJuridica()
        instancia.PJ()

