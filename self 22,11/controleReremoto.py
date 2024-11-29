class controleReremoto:
     
        def __init__(self,cor,altura,profundida,largura):
            self.cor=cor 
            self.altura=altura
            self.profundidade=profundida
            self.largura=largura

        def iniciar(self,ligar,desligar):
            if ligar== "ligar":
              print ("ligar") 
            elif desligar == "desligar":
                print ("Desligar")
         

        def mudar_calnal(self,botao):
         if botao=="+":
            print ("aumentar canal")
         elif botao=="-": 
                print ("diminuir canal") 
                      
         else: print ("valor inválido")

tvdasala=controleReremoto("vermelho",20,5,10)
tvdasala.mudar_calnal("+")

ventilador=controleReremoto("branco", 10,2,6)
ventilador.iniciar("ligar")





#diagrama de um controle
# nome
#caracteristicas
 #cor, altura,largura
#funçao
 #mudar de canal, aumentar volume+