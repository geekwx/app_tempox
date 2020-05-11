#Crianção do gui do app 

from clima import clima
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", 9)

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.titulo = Label(self.container1, text="App_clima")
        self.titulo["font"]=("Calibri", "15", "bold")
        self.titulo.pack()

        self.texto1 = Label(self.container2, text="Clique no Botao Para Busca \na  temperatura da sua regiao", font=self.fonte, width=50)
        self.texto1.pack(side=LEFT)

        self.btnBusca = Button(self.container3, text="Buscar", font=self.fonte, width=20)
        self.btnBusca["command"] = self.buscaExec
        self.btnBusca.pack()

        #Retorno da solucao do clima
        
        self.lblLocal = Label(self.container4, text="Localização", font=self.fonte, width=25)
        self.lblLocal.pack()

        self.lblDia = Label(self.container5, text="Dia", font=self.fonte, width=15)
        self.lblDia.pack()

        self.lblMin = Label(self.container6, text="Temperatura", font=self.fonte, width=15)
        self.lblMin.pack()

        self.lblMax = Label(self.container7, text="Clima", font=self.fonte, width=15)
        self.lblMax.pack()

     
    def buscaExec(self):
        coordenada = clima.pegarCoordenadas()
        local = clima.pegarCodigoLocal(coordenada['lat'], coordenada['lon'])
        climaAtual = clima.pegarclimaAgora(local['codigoLocal'], local['nomeLocal'])
        #mudando no layout
        self.lblLocal["text"]= climaAtual['nomeLocal']
        self.lblDia["text"]= "Hoje"
        self.lblMin["text"]= climaAtual['temperatura']
        self.lblMax["text"]= climaAtual['textoClima']
        print(coordenada)
        
root = Tk()
Application(root)
root.mainloop()