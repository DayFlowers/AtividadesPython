class Bola:
    def __init__ (self,circunferencia, material,cor):
        self.circunferencia=circunferencia
        self.material=material
        self.cor=cor
        
    def trocar_cor (self):
        print(self.cor)
        self.cor=input('Dgt uma cor:')
        print(self.cor)

    def trocar_material (self):
        print(self.material)
        self.material=input("qual novo material?")
        print(self.material)

bola1=Bola(4,"couro","preta")
bola1.trocar_cor()
bola1.trocar_material()

