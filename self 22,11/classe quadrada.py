class Quadrado:
    def __init__ (self,lado): #init =valores
        self.lado=lado

    def mostra_area (self):
        area = self.lado*self.lado
        print("a area do quadrado:",area) 

    def mudar_valor_lado (self):
        x=int(input("dgt o novo valor do lado:"))
        self.lado=x
        print("novovalor:",self.lado)
        area=self.lado*self.lado
        print(area)

x=int(input("dgt o valor do lado:"))
estanciar=Quadrado(x)
estanciar.mostra_area()
estanciar.mudar_valor_lado()