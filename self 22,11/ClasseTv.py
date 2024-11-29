class Tv:

    def __init__ (self,canais, volume):
        self.canais=canais
        self.volume=volume


    def mudar_canal(self):
        mudar_canalcanal= self.canal
        print(self.mudar_canal)
        x=int(input("dgt o canal:",mudar_canalcanal))
        print (x)

    def mudar_volume (self,botao):
        if botao=="+":
            print ("aumentar volume")
        elif botao=="-": 
            print ("diminuir volume") 

x=int(input("Qual novo canal"))

mudar_canal=Tv(x)
print ()
