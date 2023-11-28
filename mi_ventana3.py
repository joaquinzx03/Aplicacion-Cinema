import tkinter as tk
import requests


class Ventana_3:
    def __init__(self,ventana, get_url:str) -> None:

        self.ventana = ventana
        self.ventana.title("CARTELERA")
        self.ventana.geometry("350x450+600+200") #original: 350x450+600+200, extendida:"735x500+380+150"
        self.ventana.config(background="Black")
        self.ventana.resizable(width=False, height=False)

        self.url_snacks:str=get_url

        self.diccionario_snacks:dict = self.url_snacks.json()
        
        self.valor_total_entrada:float=0
        
        self.cantidad_entradas:int=0

        self.valor_total_snacks:float=0
        
        self.cantidad_snacks:dict={}
        self.cantidad_snacks={item: 0 for item in self.diccionario_snacks}
        
        self.crear_frames()


    def crear_frames(self)-> None:

        #FRAME ENTRADA
        self.frame_valor_entrada=tk.Frame(self.ventana, bg="grey", width=300,height=300 )
        self.frame_valor_entrada.place(x=30,y=20)

        #FRAME SNACKS
        self.frame_snacks=tk.Frame(self.ventana, bg="grey", width=300,height=400 )
        self.frame_snacks.place(x=350,y=20)

        #FRAME CARRITO
        self.frame_carrito_compras=tk.Frame(self.ventana, bg="grey", width=200,height=80 )
        self.frame_carrito_compras.place(x=55,y=350)

        self.crear_etiquetas_ventas()
    
        self.carrito_de_compras()

        self.etiquetas_snacks()


    def mostrar_snacks(self)-> None:
        
        self.ventana.geometry("745x500+380+150")
        
        self.frame_carrito_compras.place(x=55,y=375) #solo es estetica sjajsjsa


    def gestionar_total(self)-> None:
        
        self.valor_total=self.valor_total_entrada+self.valor_total_snacks

        self.total.config(text=f"Total:       ${self.valor_total}") 

    def total_entrada(self, operacion:str)-> None:

        if operacion=="suma":
        
            self.valor_total_entrada+=2450
           
            self.cantidad_entradas+=1
        else:
        
            self.valor_total_entrada-=2450
           
            self.cantidad_entradas-=1  

            if self.valor_total_entrada<0: self.valor_total_entrada=0
            
            if self.cantidad_entradas<0: self.cantidad_entradas=0

        if self.cantidad_entradas<10:
        
            self.compra.config(text=f"compra:     {self.cantidad_entradas}")              
            
        else:
        
            self.compra.config(text=f"compra:   {self.cantidad_entradas}")

        self.gestionar_total()
            

    def crear_etiquetas_ventas(self)-> None:

        #VALOR
        self.valorEntrada= tk.Label(self.frame_valor_entrada, text=" VALOR DE LA ENTRADA \n$2450",font=("Time new romans",15),
            bg="White",relief="sunken",border=5)
        self.valorEntrada.place(x=20, y=10)

        #COMPRAR
        self.compra=tk.Label(self.frame_valor_entrada, text="Compra:    0", font=("Time new romans",20),
            bg="grey",relief="groove",)
        self.compra.place(x=64, y=100 )

        #TOTAL
        self.total=tk.Label(self.frame_valor_entrada,text=f"Total:             $0",
            font=("Time new romans",20),bg="black",fg="White",relief="groove",)
        self.total.place(x=40, y=250)

        #AGREGAR SNACKS
        self.agregar_snacks=tk.Button(self.frame_valor_entrada, text="¡AGREGAR SNACKS!", bg="red",font=("Time new romans",15),
            command=lambda: self.mostrar_snacks(),cursor="hand2")
        self.agregar_snacks.place(x=40,y=180)

        #AGREGAR ENTRADA
        self.SumarEntrada= tk.Button(self.frame_valor_entrada, text="+",font=("Time new romans",14,"bold"), 
            bg="Green", relief="raised", cursor="hand2", command=lambda: self.total_entrada("suma"))
        self.SumarEntrada.place(x=222,y=100)

        #RESTAR ENTRADA
        self.RestarEntrada= tk.Button(self.frame_valor_entrada, text="-",font=("Time new romans",14,"bold"),
            bg="magenta",relief="raised",cursor="hand2",command= lambda: self.total_entrada("resta"))
        self.RestarEntrada.place(x=38, y=100)


    def ir_ventana_4(self)-> None:

        self.ventana.withdraw()


    def carrito_de_compras(self)-> None:

        self.carrito=tk.Button(self.frame_carrito_compras,text="Agregar al carrito", font=["Arial",20], bg="skyblue", 
            relief="sunken",bd=7, command=lambda: self.ir_ventana_4(),cursor="hand2")
        self.carrito.pack()
    
    
    def total_snacks(self,operacion:str,precio:float)-> None:

        for snacks in self.diccionario_snacks:
            
            if precio==self.diccionario_snacks[snacks]:
                
                if operacion=="suma":

                    self.valor_total_snacks+=float(precio)

                    self.cantidad_snacks[snacks]+=1

                else:

                    if self.cantidad_snacks[snacks]>0:

                        self.valor_total_snacks-=float(precio)

                        self.cantidad_snacks[snacks]-=1

            self.etiquetas_snacks()

        self.gestionar_total()                  
        
    
    def etiquetas_snacks(self)-> None:
        
        fila:int=0

        for snacks in self.diccionario_snacks:
            
            texto= f"{snacks} ${self.diccionario_snacks[snacks]}:    {self.cantidad_snacks[snacks]}"

            self.etiqueta_snacks=tk.Label(self.frame_snacks, text=texto,
                 font=["Arial", 15],bg="white",relief="groove",bd=5)
            self.etiqueta_snacks.grid(row=fila, column=1, sticky="w", padx=13,pady=15) 
            
            self.boton_suma_snacks=tk.Button(self.frame_snacks, text="+", font=["Arial", 10],
                bg="green",relief="groove",bd=5,cursor="hand2", 
                command=lambda x=self.diccionario_snacks[snacks]: self.total_snacks("suma",x))
            self.boton_suma_snacks.grid(row=fila, column=2,sticky="e",padx=5)
            
            self.boton_resta_snacks=tk.Button(self.frame_snacks, text="-", font=["Arial", 10],
                bg="magenta",relief="groove",bd=5,cursor="hand2",
                command=lambda x=self.diccionario_snacks[snacks]: self.total_snacks("resta",x))
            self.boton_resta_snacks.grid(row=fila, column=0,sticky="e",padx=5)

            fila+=1


            
def pseudomain()-> None:
    #ventana 2
    ventanaX=tk.Tk()
    ventanaX.geometry("500x500+400+20")
    ventanaX.config(bg="orange")
    
    #mi ventana
    def otra_ventana():
        ventanaX.withdraw()

        raiz= tk.Tk()
      
        url="http://vps-3701198-x.dattaweb.com:4000"+"/snacks"
        
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"
        headers = {"Authorization": f"Bearer {token}"}
        
        get_url = requests.get(url, headers=headers)
       

        pantalla_reserva=Ventana_3(raiz,get_url)
      
        pantalla_reserva.ventana.mainloop()

    #boton para ventana 2 a 3
    boton=tk.Button(ventanaX,text="otra ventana",command=lambda: otra_ventana(),width=30,height=10) #dsp poner el lambda
    boton.place(x=100,y=100)

    
    #mainloop de ventana3
    ventanaX.mainloop()

pseudomain()