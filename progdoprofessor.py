import sys
from tkinter import *

##################################################

class Janela(Tk): ## Questão 01: (Complete o código que declara a classe)
    __Lb_flamengo=None
    __Lb_vasco=None
    __Lb_torcida_total=None
    __Lb_pr=None
    __Lb_sc=None
    __Lb_rs=None
    __Et_flamengo_pr=None
    __Et_flamengo_sc=None
    __Et_flamengo_rs=None
    __Et_vasco_pr=None
    __Et_vasco_sc=None
    __Et_vasco_rs=None
    __Et_total_flamengo=None
    __Et_total_vasco=None
    __Bt_calc=None
    
    ## Questão 02: (Criar o construtor da classe Janela)
    def __init__(self, Str= "Janela", Cor="orange"):
        super().__init__()
        super().title(Str)
        super().configure(bg=Cor)
        
        self.inicialize()
    
    def action_Total_Flamengo(self):
        ## Questão 03: (Criar o evento que calcula o total de torcedores do Flamengo)
        fla_1 = float(self.__Et_flamengo_pr.get())
        fla_2 = float(self.__Et_flamengo_sc.get())
        fla_3 = float(self.__Et_flamengo_rs.get())
        total = fla_1 + fla_2 + fla_3
        
        self.__Et_total_flamengo.delete(0, END)
        self.__Et_total_flamengo.insert(END, f"{total:3.1f}")
       
        
    
    def action_Total_Vasco(self):
        ## Questão 04: (Criar o evento que calcula o total de torcedores do Vasco)
        vasco_1 = float(self.__Et_vasco_pr.get())
        vasco_2 = float(self.__Et_vasco_sc.get())
        vasco_3 = float(self.__Et_vasco_rs.get())
        total = vasco_1 + vasco_2 + vasco_3
        
        self.__Et_total_vasco.delete(0, END)
        self.__Et_total_vasco.insert(END, f"{total:3.1f}")
    
    def action_exit(self):
        ## Questão 05: (Qual o código necessário para encerrar o programa no canto superior direito da janela)
        self.destroy()
    
    def action_Bt_calc(self):
        ## Questão 06: (Chamar os eventos que fazem os cálculos citados em 03, 04)
        self.action_Total_Flamengo()
        self.action_Total_Vasco()
    
    def inicialize(self):
        ## Questão 07: Realize a alocação dos componentes gráficos)
        self.__Lb_flamengo= Label(self, text= "Flamengo")
        self.__Lb_vasco= Label(self, text= "Vasco")
        self.__Lb_torcida_total= Label(self, text= "Torcida total:")
        self.__Lb_pr= Label(self, text= "Paraná")
        self.__Lb_sc= Label(self, text= "Santa Catarina")
        self.__Lb_rs= Label(self, text= "Rio G. do Sul")
        self.__Et_flamengo_pr= Entry(self)
        self.__Et_flamengo_sc= Entry(self)
        self.__Et_flamengo_rs= Entry(self)
        self.__Et_vasco_pr= Entry(self)
        self.__Et_vasco_sc= Entry(self)
        self.__Et_vasco_rs= Entry(self)
        self.__Et_total_flamengo= Entry(self)
        self.__Et_total_vasco= Entry(self)
      
        
        
        self.__Bt_calc=Button(self, text='Calcular', command=self.action_Bt_calc)
        ## Questão 08: (Qual o comando que associa o botão Bt_calc ao evento
        ##              que realiza os cálculos da Questão 06 ?)
        
        ############# Grid #############
        ## Questão 09: (Acrescentar os componentes gráficos na Tela)
        self.__Lb_flamengo.grid(row=0, column=1, padx=2, pady=2)
        self.__Lb_vasco.grid(row=0, column=2, padx=2, pady=2)
        
        self.__Lb_torcida_total.grid(row=5, column=0, padx=2, pady=2)
        
        self.__Lb_pr.grid(row=1, column=0, padx=2, pady=2)
        self.__Lb_sc.grid(row=2, column=0, padx=2, pady=2)
        self.__Lb_rs.grid(row=3, column=0, padx=2, pady=2)
        
        self.__Et_flamengo_pr.grid(row=1, column=1, padx=2, pady=2)
        self.__Et_flamengo_sc.grid(row=2, column=1, padx=2, pady=2)
        self.__Et_flamengo_rs.grid(row=3, column=1, padx=2, pady=2)
        
        self.__Et_vasco_pr.grid(row=1, column=2, padx=2, pady=2)
        self.__Et_vasco_sc.grid(row=2, column=2, padx=2, pady=2)
        self.__Et_vasco_rs.grid(row=3, column=2, padx=2, pady=2)
        
        self.__Et_total_flamengo.grid(row=5, column=1, padx=2, pady=2)
        self.__Et_total_vasco.grid(row=5, column=2, padx=2, pady=2)
        
        self.__Bt_calc.grid(row=4, column=1, padx=2, pady=2)
        
        self.protocol("WM_DELETE_WINDOW", self.action_exit)

##################################################

## Questão 10: (Aloque um objeto do classe Janela e mostre-o na tela)
xanela=Janela("Torcidas de Futebol")
xanela.mainloop()
