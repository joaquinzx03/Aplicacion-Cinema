import cv2
import tkinter as tk
from tkinter import filedialog

def escanear_codigo(ruta,ventana):
    """
    toma un número de identificación (ID), busca la imagen correspondiente al código QR, la lee, intenta 
    detectar y decodificar el código QR, y luego actualiza la interfaz gráfica con el resultado. 
    Esta función se utiliza como un controlador de eventos para el botón "Escanear QR" en tu interfaz gráfica de usuario 
    (GUI) creada con la biblioteca Tkinter.
    """
    
    ruta_archivo = f"ID_{ruta}.png"

    imagen_qr = cv2.imread(ruta_archivo)
    
    try:
        detector = cv2.QRCodeDetector()
        
        texto_qr, pts_region_QR, qr_code = detector.detectAndDecode(imagen_qr)
        
        resultado = tk.Label(ventana,text=f"Información del código QR: {texto_qr}")
        
        resultado.pack(pady=10)
        
    #si la libreria tira un error:  
    except cv2.error:
        
        resultado = tk.Label(ventana,text="No se encontró ningún código QR en la imagen.")
        
        resultado.pack(pady=10)
    
        

def escanear_callback(ventana,ID_entrada):
    
    ruta = ID_entrada.get()
    
    escanear_codigo(ruta, ventana)


def main():
    ventana = tk.Tk()
    ventana.title("Escáner de QR")
    ventana.config(bg="black")

    ID= tk.Label(ventana, text="Ingrese el numero de su QR:",relief="solid", width=40)

    ID_entrada = tk.Entry(ventana)

    boton_escanear = tk.Button(ventana, text="Escanear QR", command=lambda: escanear_callback(ventana,ID_entrada))
    

    ID.pack(pady=10)
    ID_entrada.pack(pady=10)
    boton_escanear.pack(pady=10)

    ventana.mainloop()
    
main()
