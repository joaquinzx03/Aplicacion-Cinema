import tkinter as tk
import requests

#====================================================================================================================
#====================================================================================================================
class Ventana_3:
    def __init__(self,ventana3, get_url) -> None:

        self.ventana3 = ventana3
        self.ventana3.title("CARTELERA")
        self.ventana3.geometry("350x450+600+200") #original: 350x450+600+200, extendida:"735x500+380+150"
        self.ventana3.config(background="Black")
        self.ventana3.resizable(width=False, height=False)

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
        self.frame_valor_entrada=tk.Frame(self.ventana3, bg="grey", width=300,height=300 )
        self.frame_valor_entrada.place(x=30,y=20)

        #FRAME SNACKS
        self.frame_snacks=tk.Frame(self.ventana3, bg="grey", width=300,height=400 )
        self.frame_snacks.place(x=350,y=20)

        #FRAME CARRITO
        self.frame_carrito_compras=tk.Frame(self.ventana3, bg="grey", width=200,height=80 )
        self.frame_carrito_compras.place(x=55,y=350)

        self.crear_etiquetas_ventas()
    
        self.carrito_de_compras()

        self.etiquetas_snacks()


    def mostrar_snacks(self)-> None:
        
        self.ventana3.geometry("745x500+380+150")
        
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
    
            
    #IR VENTANA 4
    def ir_ventana_4(self)-> None:
        
        self.ventana3.withdraw()
        
        ventana_4=tk.Toplevel()

        informacion={
            "Pelicula":"X",
            "Sala":"X",
            "Lugar":"X",
            "Entradas":self.cantidad_entradas,
            "Monto":self.valor_total_entrada,
            "Snacks":self.cantidad_snacks,
            }
        
        informacion["Snacks"]["Monto"]=self.valor_total_snacks
        
        
        finalizar_compra=Ventana4(ventana_4,informacion)


    def carrito_de_compras(self)-> None:

        self.carrito=tk.Button(self.frame_carrito_compras,text="Agregar al carrito", font=["Arial",20], bg="skyblue", 
            relief="sunken",bd=7, command=lambda: self.ir_ventana_4(),cursor="hand2")
        self.carrito.pack()
    
#====================================================================================================================
#====================================================================================================================
class Ventana4():
    
    def __init__(self,ventana4, informacion:dict) -> None:
        
        self.ventana4=ventana4
        self.ventana4.title("Checkout")
        self.ventana4.geometry("500x700+550+50")
        self.ventana4.config(background="Black")
        self.ventana4.resizable(width=False, height=False)
        
        self.informacion:dict=informacion
        
        self.crear_frames()
        
        
    def crear_frames(self)-> None:
        
        #FRAME INFORMACION
        self.frame_informacion=tk.Frame(self.ventana4,bg="grey", width=450,height=550)
        self.frame_informacion.pack(pady=30)
        
        #FRAME PAGAR
        self.frame_ejecutar_compra=tk.Frame(self.ventana4,bg="red", width=200,height=150)
        self.frame_ejecutar_compra.pack(pady=5)
        
        self.crear_etiquetas()
        
        
    def ir_a_qr(self)-> None:
        self.ventana4.destroy()
        
        
    def crear_etiquetas(self)-> None:
        
        #TITULO general:
        self.etiqueta_titulo=tk.Label(self.frame_informacion,text="Detalles de la compra:", bg="white",
                font=["Arial",20],bd=8, relief="sunken" )
        self.etiqueta_titulo.place(x=60,y=10)
        
        #TITULO De Entradas:
        self.etiqueta_titulo_entrada=tk.Label(self.frame_informacion,text="Entradas:", bg="white",
                font=["Arial",20],bd=5, relief="groove" )
        self.etiqueta_titulo_entrada.place(x=5,y=80)
        
        
        #TITULO De Snacks:
        self.etiqueta_titulo_snacks=tk.Label(self.frame_informacion,text="Snacks:", bg="white",
                font=["Arial",20],bd=5, relief="groove" )
        self.etiqueta_titulo_snacks.place(x=260,y=80)
        
        fila:int=0
        
        #ETIQUETA De Entradas:
        for elemento in self.informacion:
            
            if elemento!="Snacks":
                texto=f"{elemento}: {self.informacion[elemento]}"
                
                self.etiqueta_informacion_entrada=tk.Label(self.frame_informacion,text=texto,
                    font=["Arial",15],bd=3, relief="sunken",bg="grey")
                self.etiqueta_informacion_entrada.place(x=5,y=160+60*fila)            
                
                fila+=1    
     
        fila:int=0
               
        #ETIQUETA De Snacks:
        for elemento in self.informacion:
           
            if elemento=="Snacks":
           
                for snacks in self.informacion[elemento]:
                    if self.informacion[elemento][snacks]!=0:
                        texto=f"{snacks}: {self.informacion[elemento][snacks]}"
                        
                        self.etiqueta_informacion_snacks=tk.Label(self.frame_informacion,text=texto,
                            font=["Arial",15],bd=3, relief="sunken",bg="grey")
                        self.etiqueta_informacion_snacks.place(x=260,y=150+50*fila)

                        fila+=1
                    
        #ETIQUETA total:
        total=self.informacion["Snacks"]["Monto"]+self.informacion["Monto"]
        
        self.etiqueta_total=tk.Label(self.frame_informacion,text=f"\nTOTAL:  {total} \n",
                font=["Arial",13,"bold"], relief="sunken",bg="black",fg="White",bd=10)
        self.etiqueta_total.place(x=5,y=470)
        
        #BOTON pagar
        self.boton_ejecutar_compra=tk.Button(self.frame_ejecutar_compra, text="Pagar",
            bg="red",fg="black",font={"Arial", 25},relief="groove",bd=5,width=40,height=2,
            command=lambda: self.ir_a_qr())
        self.boton_ejecutar_compra.pack()
        

            
def pseudomain()-> None:
    
    #VENTANA 3
    ventana3=tk.Tk()
    
    url="http://vps-3701198-x.dattaweb.com:4000"+"/snacks" 
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"
    headers = {"Authorization": f"Bearer {token}"}    
    get_url = requests.get(url, headers=headers)
       
    pantalla_reserva=Ventana_3(ventana3,get_url)
    
    pantalla_reserva.ventana3.mainloop()
    


pseudomain()