import tkinter as tk
import requests
from PIL import Image, ImageTk
import base64
from io import BytesIO

class Ventana:
    
    def __init__(self, ventana) -> None:
        self.ventana_1 = ventana
        self.ventana_1.geometry("800x500+200+100")
        self.ventana_1.config(bg= "black")
        self.ventana_1.title("Demostración")
        self.ventana_1.resizable(False,False)
        
        self.crear_frames()
    
    def crear_frames(self) -> None:
        self.pantalla_ventana_1_num1 = tk.Frame(self.ventana_1, bg= "gray", width=400, height=400, relief= "groove", bd= 4)
        self.pantalla_ventana_1_num1.place(x= 0, y= 100)

        self.pantalla_ventana_1_num2 = tk.Frame(self.ventana_1, bg= "gray", width=400, height=430, relief= "groove", bd= 4)
        self.pantalla_ventana_1_num2.place(x=400, y= 0)
    
        self.crear_etiquetas()    
    
    def crear_texto_informativo(self, posicion: int) -> str:

        self.url= "http://vps-3701198-x.dattaweb.com:4000/movies/3"

        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"

        self.headers = {"Authorization":f"Bearer {self.token}"}

        self.response= requests.get(self.url, headers=self.headers)

        self.dict_poster = self.response.json()
    
        self.claves_texto = ["name", "synopsis", "gender", "duration", "actors", "directors", "rating"]
        self.reemplazo_claves_texto = ["Titulo: ", "Sinopsis: ", "Género: ", "Duración: ","Actores: ", "Directores: ", "Rating: " ]
        self.texto_completo = f"{self.reemplazo_claves_texto[posicion]}{self.dict_poster[self.claves_texto[posicion]]}" 

        return self.texto_completo
    
    def crear_imagen(self) -> any:
        self.url_api = 'http://vps-3701198-x.dattaweb.com:4000/posters/3'
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU'
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.response = requests.get(self.url_api, headers=self.headers)
        
        self.codigo_base64 = self.response.content.decode("utf-8")
        self.codigo_base64 = self.codigo_base64.split(",", 1)[1]
        
        self.longitud_requerida = len(self.codigo_base64) + (4 - len(self.codigo_base64) % 4) % 4
        self.codigo_base64_padded = self.codigo_base64.ljust(self.longitud_requerida, "=")
        
        self.imagen_bytes = base64.b64decode(self.codigo_base64_padded)
        self.imagen_pillow = Image.open(BytesIO(self.imagen_bytes))
        self.imagen_pillow = self.imagen_pillow.resize((387,387))
        self.tk_imagen = ImageTk.PhotoImage(self.imagen_pillow)
        return self.tk_imagen
        
    def crear_etiquetas(self) -> None:
        
        self.etiqueta_imagen = tk.Label(self.pantalla_ventana_1_num1, image= self.crear_imagen())
        self.etiqueta_imagen.pack()
        

        for i in range(7):
            self.descripcion= tk.Label(self.pantalla_ventana_1_num2,text= self.crear_texto_informativo(i),width=45,height=1, font= ["Arial", 10], anchor= "w")
            if i == 1:
                self.descripcion = tk.Text(self.pantalla_ventana_1_num2, wrap=tk.WORD, width=52, height=16, font=["Arial", 10])
                self.descripcion.insert(tk.END, self.crear_texto_informativo(i))
                self.descripcion.config(state=tk.DISABLED)
                self.descripcion.place(x=12,y=30)
            elif i == 0:
                self.descripcion.place(x=12,y=5)
            else:
                self.descripcion.place(x=12,y=245 + 25*i)
        
        self.crear_botones()
    
    def crear_botones(self) -> None:
        self.boton0_ir_a_pantalla_3= tk.Button(self.ventana_1, bg= "gray", text= "boton compra (dirige a pantalla 3)", fg= "black", font= ("Arial", 15), relief= "groove", bd = 15, cursor="hand2")
        self.boton0_ir_a_pantalla_3.place(x=433, y=432)
        
        self.boton1_ir_a_pantalla_1 = tk.Button(self.ventana_1, bg= "gray", text= "<= Volver", fg= "black", font= ("Arial", 15), relief= "groove", bd= 15, cursor= "hand2")
        self.boton1_ir_a_pantalla_1.place(x= 30, y= 15)
        

def main() -> None:
    ventana_1 = tk.Tk()
    Demostracion = Ventana(ventana_1)
    ventana_1.mainloop()
main()
