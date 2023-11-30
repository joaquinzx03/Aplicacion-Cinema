import tkinter as tk
from PIL import ImageTk, Image
import requests
import base64
from io import BytesIO

class Pantalla_principal:
    
    def __init__(self, master):
        
        self.master = master
        self.master.geometry("900x900")
        self.master.title("Pantalla Principal")
        self.master.config(bg = "light gray")
        self.master.resizable(False, False)
        
        
        self.creador_marcos()
        self.buscador_con_boton()
        self.creacion_botones()
        
    def creador_marcos(self):
        
        lista_contenedores = []
        
        fila = 0
        columna = 0
        
        for _ in range(9):
                
            self.contenedores = tk.Frame(self.master, bg = "light gray", width = 300, height = 260)
            
            self.contenedores.grid(row = fila, column = columna)
            
            lista_contenedores.append(self.contenedores)
            
            columna += 1
            
            if fila == 0 and columna == 3:
                
                fila = 1
                columna = 0
            
            elif fila == 1 and columna == 3:
                
                fila = 2 
                columna = 0
            
        self.creador_canvas_imagenes(lista_contenedores)

    def creacion_botones(self):
        
        posicion_y = 200
        
        for n in range(1,7):
            
            posicion_x = 100
            
            if n % 2 == 0: posicion_x = 700
            
            if n == 3: posicion_y = 460
            
            elif n == 5: posicion_y = 720
            
            url_info_pelis_botones_ver = "http://vps-3701198-x.dattaweb.com:4000/movies/" + f"{n}"
        
            token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"
            headers= {"Authorization": f"Bearer {token}"} 
        
            info_pelis_botones_ver = requests.get(url_info_pelis_botones_ver, headers = headers)
                
            self.botones = tk.Button(self.master, text = "Ver", width = 10, height = 1, bd = "7",
                                    command = lambda dict_boton_ver = info_pelis_botones_ver.json():self.ir_pagina_secundaria(dict_boton_ver))
            
            self.botones.place(x = posicion_x, y = posicion_y)        
        
            
    def ir_pagina_secundaria(self, dict_info_peliculas):
        
        self.master.withdraw()
        
        ventana_secundaria = tk.Toplevel()  
        
        diccionario_info_peliculas = dict_info_peliculas
        print(dict_info_peliculas)
        
    def verificar_pelicula(self, ingreso_del_usuario): 
        
        for i in range(1, 7):
            url_info_pelis = "http://vps-3701198-x.dattaweb.com:4000/movies/" + f"{i}"
            
            token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"
            headers= {"Authorization": f"Bearer {token}"}
            
            self.info_pelis = requests.get(url_info_pelis, headers = headers)
            
            self.nombres_pelis = (self.info_pelis.json()["name"])
            
            self.nombres_pelis_minusculas = self.nombres_pelis.lower()
            
            if self.nombres_pelis_minusculas == ingreso_del_usuario:
            
                self.ir_pagina_secundaria(self.info_pelis.json())
            
    def buscador_con_boton(self):
        
        ingreso_del_usuario = tk.StringVar(self.master)
        
        self.entrada_de_texto = tk.Entry(self.master, width = 37,  fg = "White", bg = "black", justify = "center", textvariable = ingreso_del_usuario)
        self.entrada_de_texto.place(x = 340, y = 300)
        
        
        self.boton_buscar = tk.Button(self.master, text = "Buscar Película",
                                    width = 15, command = lambda: self.verificar_pelicula( ingreso_del_usuario.get()))
        self.boton_buscar.place(x = 395, y = 350)
        
        self.etiqueta_ubicacion = tk.Label(self.master, text = "Usted está en el cine de { ubicacion }", bg = "light gray",
                                        justify = "center").place(x = 355, y = 730)
        
    def crear_imagen(self) -> any:
        self.url_api = 'http://vps-3701198-x.dattaweb.com:4000/posters/2'
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU'
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.response = requests.get(self.url_api, headers=self.headers)
        
        self.codigo_base64 = self.response.content.decode("utf-8")
        self.codigo_base64 = self.codigo_base64.split(",", 1)[1]
        
        self.longitud_requerida = len(self.codigo_base64) + (4 - len(self.codigo_base64) % 4) % 4
        self.codigo_base64_padded = self.codigo_base64.ljust(self.longitud_requerida, "=")
        
        self.imagen_bytes = base64.b64decode(self.codigo_base64_padded)
        self.imagen_pillow = Image.open(BytesIO(self.imagen_bytes))
        self.tk_imagen = ImageTk.PhotoImage(self.imagen_pillow)
        return self.tk_imagen
        
    def creador_canvas_imagenes(self, lista_contenedores):
        
        lista_imagenes = []
        
        for i in (1,0,2,3,0,4,5,0,6):
            
            if i == 0 or i == 0: 
                lista_imagenes.append(0)
                continue
            
            self.url_api = 'http://vps-3701198-x.dattaweb.com:4000/posters/' + f"{i}"
            self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU'
            self.headers = {'Authorization': f'Bearer {self.token}'}
            self.response = requests.get(self.url_api, headers=self.headers)
            
            self.codigo_base64 = self.response.content.decode("utf-8")
            self.codigo_base64 = self.codigo_base64.split(",", 1)[1]
            
            self.longitud_requerida = len(self.codigo_base64) + (4 - len(self.codigo_base64) % 4) % 4
            self.codigo_base64_padded = self.codigo_base64.ljust(self.longitud_requerida, "=")
            
            self.imagen_bytes = base64.b64decode(self.codigo_base64_padded)
            
            lista_imagenes.append(self.imagen_bytes)
            # self.imagen_pillow = Image.open(BytesIO(self.imagen_bytes))
            # self.tk_imagen = ImageTk.PhotoImage(self.imagen_pillow)

            
            
            # lista_imagenes = ['imagenes\\imagen_boogeyman.jpg',  'imagenes\\cinema.jpg', 'imagenes\\coco.jpg', 'imagenes\\exorcista.jpg', 0,
            #             'imagenes\\exorcista_papa.jpg', 'imagenes\\el-justiciero.jpg', 0, 'imagenes\\señor_de_los_anillos.jpg']  
            
        for i in range(len(lista_imagenes)):
            if lista_imagenes[i] == 0: continue
            
            canvas_general = tk.Canvas(lista_contenedores[i], bg = "black", height = 260, width = 300, borderwidth = 0, highlightthickness = 0)
            canvas_general.grid(row = 0, column = 0, sticky = "nesw", padx = 0, pady = 0)
            
            imagen_en_canvas = Image.open(BytesIO(lista_imagenes[i]))
            canvas_general.image = ImageTk.PhotoImage(imagen_en_canvas.resize((135, 192), Image.LANCZOS))
            canvas_general.create_image((300 - 135) / 2, (200 - 192) / 2, image = canvas_general.image, anchor = 'nw')
            


def main():
    ventana_principal = tk.Tk()

    app = Pantalla_principal(ventana_principal)
    ventana_principal.mainloop()

main()