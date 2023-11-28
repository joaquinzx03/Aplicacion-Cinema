import tkinter as tk 

class Ventana4():
    
    def __init__(self,ventana, informacion) -> None:
        
        self.ventana=ventana
        self.ventana.title("Checkout")
        self.ventana.geometry("500x700+550+50")
        self.ventana.config(background="Black")
        self.ventana.resizable(width=False, height=False)
        
        self.informacion=informacion
        
        self.crear_frames()
        
    def crear_frames(self):
        
        #FRAME INFORMACION
        self.frame_informacion=tk.Frame(self.ventana,bg="grey", width=450,height=550)
        self.frame_informacion.pack(pady=30)
        
        #FRAME PAGAR
        self.frame_ejecutar_compra=tk.Frame(self.ventana,bg="red", width=200,height=150)
        self.frame_ejecutar_compra.pack(pady=5)
        
        self.crear_etiquetas()
        
    def ir_a_qr(self):
        self.ventana.destroy()
        
    def crear_etiquetas(self):
        
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
        
        fila=0
        
        #ETIQUETA De Entradas:
        for elemento in self.informacion:
            
            if elemento!="Snacks":
                texto=f"{elemento}: {self.informacion[elemento]}"
                
                self.etiqueta_informacion_entrada=tk.Label(self.frame_informacion,text=texto,
                    font=["Arial",15],bd=3, relief="sunken",bg="grey")
                
                if elemento!="Monto":
                    self.etiqueta_informacion_entrada.place(x=5,y=160+60*fila)
                else:
                    self.etiqueta_informacion_entrada.place(x=5,y=160+65*fila)
                    
                fila+=1    
     
        fila=0
               
        #ETIQUETA De Entradas:
        for elemento in self.informacion:
            if elemento=="Snacks":
                for snacks in self.informacion[elemento]:
                    
                    texto=f"{snacks}: {self.informacion[elemento][snacks]}"
                    self.etiqueta_informacion_snacks=tk.Label(self.frame_informacion,text=texto,
                        font=["Arial",15],bd=3, relief="sunken",bg="grey")
                    
                    self.etiqueta_informacion_snacks.place(x=260,y=150+50*fila)

                    
                    fila+=1
                    
        #ETIQUETA total:
        self.etiqueta_total=tk.Label(self.frame_informacion,text="\nTOTAL:  xxxxx-x\n",
                font=["Arial",13,"bold"], relief="sunken",bg="black",fg="White",bd=10)
        self.etiqueta_total.place(x=5,y=470)
        
        #BOTON pagar
        self.boton_ejecutar_compra=tk.Button(self.frame_ejecutar_compra, text="Pagar",
            bg="red",fg="black",font={"Arial", 25},relief="groove",bd=5,width=40,height=2,
            command=lambda: self.ir_a_qr())
        self.boton_ejecutar_compra.pack()
        
            
        
ventana_4=tk.Tk()

informacion={
    "Pelicula":"x",
    "Sala": "x",
    "Lugar":"x",
    "Cantidad de \n entradas": "x",
    "Monto":"$0",
    
    "Snacks":{
        "doritos":"x",
        "popcorn_xl":"x",
        "popcorn_xxl":"x",
        "papas_fritas":"x",
        "coca_cola_xl":"x",
        "coca_cola_xxl":"x",
        "chocolate 250g":"x"
        }
      }
    

informacion["Snacks"]["Monto"]="$0"

finalizar_compra=Ventana4(ventana_4,informacion)

finalizar_compra.ventana.mainloop()