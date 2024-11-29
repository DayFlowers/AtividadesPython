"""class Super:
    def hello(self):
        print ("Olá, sou a superclasse")

class Sub(Super):
    def hello (self):
        print ("Olá sou a subclasse!")

class Subsub(Sub):
    def hello (self):
        print("Olá, sou uma subsubclasse!")

teste= subsub()
teste.hello()"""

class Pessoa:
    def __init__(self):
        self.nome=(input("Digite Seu nome: "))
        self.fone=(input("Qual seu telefone?"))
        self.estado=(input("Qual estado?"))
        self.cidade=(input("qual sua cidade?"))
        self.bairro=(input("qual seu bairro?"))
        self.email=(input("qual seu email?"))
        
        
class PFisica(Pessoa):
    def PF(self):
        self.cpf=(input("Qual seu cpf?"))
        self.estadocivil=(input("Qual seu estado civil?"))
        self.rg=(input("qual seu rg?"))
        

class PJuridica(Pessoa):
    def PJ (self):
        self.cnpj=(input("Qual o CNPJ da empresa?"))
        self.natureza=(input("Qual a natureza jurídica da empresa?"))
