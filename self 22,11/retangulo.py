class retangulo:
    def __init__ (self,ladoA,ladoB): #init =valores
        self.ladoA=ladoA
        self.ladoB=ladoB
        
    

    def mostra_area (self):
        area = (self.ladoA+self.ladoB)*2
        print(area) 

    def mudar_valor_lado (self,lnovoA,lnovoB):
        self.ladoA=lnovoA
        self.ladoB=lnovoB
        
        print(self.lnovoA,self.lnovoB)
        area=(self.ladoA+self.ladoB)*2
        print(area)

estanciar=retangulo(4,4)
estanciar.mostra_area()
estanciar.mudar_valor_lado(6,6)