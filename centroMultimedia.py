#-*- coding: utf-8 -*-

#********** Proyecto final de Fundamentos de Sistemas Embebidos ************
#************* CENTRO MULTIMEDIA ***************
#	Autores:
#		Colohua Carvajal Daniela
#		Corona Carrillo Emanuel
#		Cruz Plata Eduardo
#		Higareda López Carlos A.
#	Fecha: 15/05/2022
#	Licencia: MIT License

from tkinter import *
from tkinter import ttk
import pygame
from pygame import mixer
import webbrowser
import ctypes
import os
import vlc
import time
from getpass import getuser
import pathlib
from PIL import Image,ImageTk
from playsound import playsound
import audioread
import mutagen

#Cargamos el cdll para arreglar el correcto uso del display
x11 = ctypes.cdll.LoadLibrary('libX11.so')
x11.XInitThreads()

#Función para abrir Spotify con el navegador chromium.
def abrir_Spotify():
	navegador=webbrowser.get("chromium-browser")
	#navegador=webbrowser.get("chromium")
	#navegador.open("https://open.spotify.com/",new=2, autoraise=True)
	navegador.open("https://accounts.spotify.com/es/login",new=2, autoraise=True)

#Función para abrir apple music con el navegador chromium.
def abrir_apple():
	#navegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	navegador.open("https://www.apple.com/mx/apple-music/",new=2, autoraise=True)

#Función para abrir Deezer con el navegador chromium.
def abrir_Deezer():
	#navegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	navegador.open("https://www.deezer.com/us/login",new=2, autoraise=True)

#Función para abrir Google Music con el navegador chromium.
def abrir_googleMusic():
	#navegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	navegador.open("https://music.youtube.com/",new=2, autoraise=True)

#Funcion para abrir Youtube con el navegador chromium
def abrir_youtube():
	#vavegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	vavegador.open("https://www.youtube.com/", new=2, autoraise=True)

#Función para abrir con el navegador chromium.
def abrir_Blim():
	#navegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	#navegador.open("https://www.blim.com/inicio",new=2, autoraise=True)
	navegador.open("https://www.blim.com/cuenta/ingresar",new=2, autoraise=True)

#Función para abrir Disney Plus con el navegador chromium.
def abrir_Disney():
	#navegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	navegador.open("https://www.disneyplus.com/login/",new=2, autoraise=True)

#Función para abrir HBO con el navegador chromium.
def abrir_HBO():
	#navegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	#navegador.open("https://www.hbomax.com/mx/es",new=2, autoraise=True)
	navegador.open("https://play.hbomax.com/login",new=2, autoraise=True)

#Función para abrir con el navegador chromium.
def abrir_Netflix():
	#navegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	#navegador.open("https://www.netflix.com/browse",new=2, autoraise=True)
	navegador.open("https://www.netflix.com/mx/login",new=2, autoraise=True)

#Función para abrir Hulu con el navegador chromium.
def abrir_hulu():
	#navegador=webbrowser.get("chromium")
	navegador=webbrowser.get("chromium-browser")
	navegador.open("https://www.hulu.com/welcome?orig_referrer=https%3A%2F%2Fwww.google.com%2F",new=2, autoraise=True)

#Función que despliega las usbs disponibles.
def leer_usbs(root):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana 
	pantalla_usbs = Tk()
	pantalla_usbs.title("USBs disponibles")
	pantalla_usbs.attributes('-fullscreen', True) #Maximiza la pantalla
	#pantalla_usbs.geometry('1100x700')
	pantalla_usbs.config(bg="#8dd5a6")

	#Se obtiene el nombre del usuario
	user=getuser()
	#Se especifica el directorio que contiene las usb
	path="/media/"+user+"/"
	
	#Creamos una lista con todos los archivos dentro de la usb
	usbs = os.listdir(path)
	#Se cuentan las usbs disponibles
	total_usbs = len(usbs)
	botonUsb = []
	pos_x = 100
	pos_y = 100
	
	if total_usbs > 0:
		if total_usbs >= 1:
			boton_Usb1=Button(pantalla_usbs,text=usbs[0],bg="#F64A5C", command=lambda:info_usbs(pantalla_usbs,usbs[0]))
			boton_Usb1.place(x=100,y=100)
			if total_usbs >=2:
				boton_Usb2=Button(pantalla_usbs,text=usbs[1],bg="#F64A5C", command=lambda:info_usbs(pantalla_usbs,usbs[1]))
				boton_Usb2.place(x=100,y=200)
				if total_usbs >= 3:
					boton_Usb3=Button(pantalla_usbs,text=usbs[2],bg="#F64A5C", command=lambda:info_usbs(pantalla_usbs, usbs[2]))
					boton_Usb3.place(x=100,y=300)
	else:
		print("No hay dispositivos conectados")
	#Boton para regresar a la pantalla anterior
	im_regresar=PhotoImage(file='atras_logo.png')
	boton_atras=Button(pantalla_usbs,image=im_regresar,height=150, width=150,command=lambda:menu(pantalla_usbs))
	boton_atras.place(x=800,y=500)
	
	#Se detectan nuevos dispositivos
	try:
		while True:
			detecta_usb = os.listdir(path)
			#NO hubo nuevos dispositivos
			if total_usbs == len(detecta_usb):
				pantalla_usbs.update_idletasks()
				pantalla_usbs.update()
			else:
				#Se actualiza la pantalla
				leer_usbs(pantalla_usbs)
	except:
		print("Actualizacion de dispositivos")
	
	pantalla_usbs.mainloop()

def info_usbs(root,nombre):
	root.destroy()
	pantalla_infoUSB = Tk()
	titulo = "Informacion de USB " + nombre
	pantalla_infoUSB.title(titulo)
	pantalla_infoUSB.attributes('-fullscreen', True) #Maximiza la pantalla
	#geometry('1100x700')
	pantalla_infoUSB.config(bg="#e89541")

	im_music=PhotoImage(file='music_logo.png')
	boton_music=Button(pantalla_infoUSB,image=im_music,height=150, width=150, command=lambda:muestra_musica(pantalla_infoUSB,nombre))
	boton_music.place(x=200,y=210)

	im_image=PhotoImage(file='image_logo.png')
	boton_image=Button(pantalla_infoUSB,image=im_image,height=150, width=150, command=lambda:muestra_imagen(pantalla_infoUSB,nombre))
	boton_image.place(x=400,y=210)

	im_video=PhotoImage(file='video_logo.png')
	boton_video=Button(pantalla_infoUSB,image=im_video,height=150, width=150, command=lambda:muestra_video(pantalla_infoUSB,nombre))
	boton_video.place(x=600,y=210)

	#Boton para regresar a la pantalla anterior
	im_regresar=PhotoImage(file='atras_logo.png')
	boton_atras=Button(pantalla_infoUSB,image=im_regresar,height=150, width=150,command=lambda:leer_usbs(pantalla_infoUSB))
	boton_atras.place(x=800,y=500)

	pantalla_infoUSB.mainloop()

def next_audio(numero, audios,path):
	if numero != len(audios)-1:
		numero +=1
		print("Reproduciendo audio", numero)
		mixer.init()
		mixer.music.load(path+audios[numero])
		mixer.music.set_volume(0.3)
		mixer.music.play()

def terminar_rep(root):
	root.destroy()

def crea_reproductor(root, path, archivos_music,nombre):
	
	for i in range(-1,len(archivos_music)):
	
		audio = mutagen.File(path+archivos_music[i])
		duracion = audio.info.length
		min, seg = divmod(duracion,60)
		min, seg = int(min), int(seg)
		tt=min*60 +seg
		next_audio(i,archivos_music,path)
		time.sleep(tt-5)
	muestra_musica(root,nombre)

def nueva_rep(root,path,archivos_music,nombre):
	crea_reproductor(root,path,archivos_music,nombre)

def muestra_musica(root,nombre):
	root.destroy()
	pantalla_musica = Tk()
	pantalla_musica.title("Reproductor")
	pantalla_musica.attributes('-fullscreen', True) #Maximiza la pantalla
	#geometry('1100x700')
	pantalla_musica.config(bg="#e89541")

	pygame.mixer.init()

	s=True
	#Se obtiene el nombre del usuario
	user=getuser()
	#Se especifica el directorio que contiene las usb
	path="/media/"+user+"/" + nombre+"/"
	directorio = pathlib.Path(path)
	letters=4
	archivos_music=[]
	for fichero in directorio.iterdir():
		formato = fichero.suffix
		if formato == ".mp3":
			nombre_archivo=str(fichero)
			archivos_music.append(nombre_archivo[len(path):])
	
	for audio in archivos_music:
			titulo=Label(pantalla_musica,text=audio)
			titulo.pack()
	sigue = True

	boton_atras=Button(pantalla_musica,text="INICIAR",height=5, width=20,command=lambda:nueva_rep(pantalla_musica,path,archivos_music,nombre))
	boton_atras.place(x=150,y=50)
	
	#Boton para regresar a la pantalla anterior
	im_regresar=PhotoImage(file='atras_logo.png')
	boton_atras=Button(pantalla_musica,image=im_regresar,height=150, width=150,command=lambda:info_usbs(pantalla_musica,nombre))
	boton_atras.place(x=800,y=500)

	pantalla_musica.mainloop()

def abre_imagen(path, archivos):
	for imagen in archivos:
		#Asignamos la ruta del archivo al reproductor
		media = vlc.MediaPlayer(path+imagen)
		#Reproducimos el archivo asignado
		media.play()
		#Esperamos tres segundos.
		time.sleep(3)
		#Detenemos el reproductor.
		media.stop()

def muestra_imagen(root,nombre):
	root.destroy()
	pantalla_imagen = Tk()
	pantalla_imagen.title("Archivos de Imagen")
	pantalla_imagen.attributes('-fullscreen', True) #Maximiza la pantalla
	#geometry('1100x700')
	pantalla_imagen.config(bg="#e89541")

	#Se obtiene el nombre del usuario
	user=getuser()
	#Se especifica el directorio que contiene las usb
	path="/media/"+user+"/" + nombre+"/"
	directorio = pathlib.Path(path)
	letters=4
	archivos_image=[]
	for fichero in directorio.iterdir():
		formato = fichero.suffix
		if formato == ".jpg" or formato==".png" or formato == ".gif":
			nombre_archivo=str(fichero)
			archivos_image.append(nombre_archivo[len(path):])
	
	abre_imagen(path,archivos_image)
	
	#Boton para regresar a la pantalla anterior
	im_regresar=PhotoImage(file='atras_logo.png')
	boton_atras=Button(pantalla_imagen,image=im_regresar,height=150, width=150,command=lambda:info_usbs(pantalla_imagen,nombre))
	boton_atras.place(x=800,y=500)

	pantalla_imagen.mainloop()

def lista_video(root,videos,nombre):
	root.destroy()
	pantalla_video = Tk()
	pantalla_video.title("Archivos de Video")
	pantalla_video.attributes('-fullscreen', True) #Maximiza la pantalla
	#geometry('1100x700')
	pantalla_video.config(bg="#e89541")
	
	nombre_titulo=[]
	botones = []
	for i in range(len(videos)):
		nombre_titulo.append("text"+str(i))
		botones.append("boton"+str(i))

	for i in range(len(nombre_titulo)):
		nombre_titulo[i]=Label(pantalla_video,text=str(i) + " --> " + videos[i])
		nombre_titulo[i].pack()
		#Boton para seleccionar archivo
	
	#seleccionar=Text(pantalla_video,height=1, width=5)
	#seleccionar.pack()
	boton_sel=Button(pantalla_video, height=1, width=10, text="Seleccionar", command=lambda:abre_video(pantalla_video,path,videos))
	boton_sel.pack()

	#Boton para regresar a la pantalla anterior
	im_regresar=PhotoImage(file='atras_logo.png')
	boton_atras=Button(pantalla_video,image=im_regresar,height=150, width=150,command=lambda:info_usbs(pantalla_video,nombre))
	boton_atras.place(x=800,y=500)

	pantalla_video.mainloop()

def reproduce_videos(root,path,archivos):

	for video in archivos:
		vlc_instance = vlc.Instance()
		player = vlc_instance.media_player_new()
		media = vlc_instance.media_new(path+video)
		player.set_media(media)
		player.play()
		time.sleep(1.5)
		duration = player.get_length() / 1000
		time.sleep(duration)
		player.stop()

def muestra_video(root,nombre):
	root.destroy()
	pantalla_opciones = Tk()
	pantalla_opciones.title("Opciones de reproduccion")
	pantalla_opciones.attributes('-fullscreen', True) #Maximiza la pantalla
	#geometry('1100x700')
	pantalla_opciones.config(bg="#e89541")

	#Se obtiene el nombre del usuario
	user=getuser()
	#Se especifica el directorio que contiene las usb
	path="/media/"+user+"/" + nombre+"/"
	directorio = pathlib.Path(path)
	letters=4
	archivos_video=[]
	for fichero in directorio.iterdir():
		formato = fichero.suffix
		if formato == ".mp4" or formato==".wave":
			nombre_archivo=str(fichero)
			archivos_video.append(nombre_archivo[len(path):])
		
	#Boton para reproducir todos los videos
	boton_todos=Button(pantalla_opciones,text="Reproducir todos",height=5, width=15,command=lambda:reproduce_videos(pantalla_opciones,path,archivos_video))
	boton_todos.place(x=200,y=200)
	nombre_titulo=[]
	botones = []
	for i in range(len(archivos_video)):
		nombre_titulo.append("text"+str(i))
		botones.append("boton"+str(i))
	#Boton para elegir video
	boton_elegir=Button(pantalla_opciones,text="Elegir video",height=5, width=15, command=lambda:lista_video(pantalla_opciones,archivos_video,nombre))
	boton_elegir.place(x=500,y=200)

	#Boton para regresar a la pantalla anterior
	im_regresar=PhotoImage(file='atras_logo.png')
	boton_atras=Button(pantalla_opciones,image=im_regresar,height=150, width=150,command=lambda:info_usbs(pantalla_opciones,nombre))
	boton_atras.place(x=800,y=500)

	pantalla_opciones.mainloop()
#Función para la pantalla del menu principal
def menu(root):
	#Se destruye la ventana recibida.
	root.destroy()
	#Inicializa la ventana, se especifican las dimensiones y el color
	pantalla_menu = Tk()
	pantalla_menu.title("Centro Multimedia")
	pantalla_menu.attributes('-fullscreen', True) #Maximiza la pantalla
	#geometry('1100x700')
	pantalla_menu.config(bg="#8dc3d5")

	#Crea boton para abrir spotify
	im_spotify=PhotoImage(file='spotify_logo.png')
	boton_Spotify=Button(pantalla_menu,image=im_spotify, height=150, width=150,command=abrir_Spotify)
	boton_Spotify.place(x=20,y=30) 

	#Crea boton que para abrir apple music
	im_apple=PhotoImage(file='appleMusic_logo.png')
	boton_apple=Button(pantalla_menu,image=im_apple,height=150, width=150,command=abrir_apple)
	boton_apple.place(x=200,y=30) 
	
	#Se crea el botón para abrir deezer
	im_deezer=PhotoImage(file='Deezer_logo.png')
	boton_Deezer=Button(pantalla_menu,image=im_deezer, height=150, width=150,command=abrir_Deezer)
	boton_Deezer.place(x=380,y=30)

	#Boton para google music
	im_googleM=PhotoImage(file='googleMusic_logo.png')
	boton_googleM=Button(pantalla_menu,image=im_googleM,height=150, width=150,command=abrir_googleMusic)
	boton_googleM.place(x=560,y=30)
    
	#Boton para youtube
	im_youtube=PhotoImage(file='youtubeMusic_logo.png')
	boton_youtube=Button(pantalla_menu,image=im_youtube,height=150, width=150,command=abrir_youtube)
	boton_youtube.place(x=740,y=30)
	
	#boton para blim
	im_blim=PhotoImage(file='blim_logo.png')
	boton_blim=Button(pantalla_menu,image=im_blim,height=150, width=150,command=abrir_Blim)
	boton_blim.place(x=920,y=30)

	#Boton para disney
	im_disney=PhotoImage(file='Disney+_logo.png')
	boton_disney=Button(pantalla_menu,image=im_disney,height=150, width=150,command=abrir_Disney)
	boton_disney.place(x=200,y=210)

	#boton para hbo
	im_hbo=PhotoImage(file='hboGo_logo.png')
	boton_HBO=Button(pantalla_menu,image=im_hbo,height=150, width=150,command=abrir_HBO)
	boton_HBO.place(x=380,y=210)

	#boton para netflix
	im_netflix=PhotoImage(file='netflix_logo.png')
	boton_Netflix=Button(pantalla_menu,image=im_netflix,height=150, width=150,command=abrir_Netflix)
	boton_Netflix.place(x=560,y=210)
	
	#Boton para para hulu
	im_hulu=PhotoImage(file='hulu_logo.png')
	boton_hulu=Button(pantalla_menu,image=im_hulu,height=150, width=150,command=abrir_hulu)
	boton_hulu.place(x=740,y=210)

	#Boton para usb
	im_usb=PhotoImage(file='usb_im.png')
	boton_USB=Button(pantalla_menu,image=im_usb, height=150, width=150,command=lambda:leer_usbs(pantalla_menu))
	boton_USB.place(x=430,y=410) 

	#boton para salir  
	im_salir=PhotoImage(file='salir_logo.png') 
	botonSalir=Button(pantalla_menu,image=im_salir,height=150, width=150,command=lambda:pantalla_menu.destroy())
	botonSalir.place(x=800,y=500) 
	
	pantalla_menu.mainloop()

#Función principal
if __name__ == "__main__":
	#Inicializa ventana de bienvenida
	pantalla_inicio = Tk()
	pantalla_inicio.title("Inicio")
	pantalla_inicio.attributes('-fullscreen', True) #Maximiza la pantalla
	#geometry('1100x700')
	pantalla_inicio.config(bg="#8dc3d5")

	#Crea etiqueta y se asigna la ventana y el texto a mostrar
	titulo=Label(pantalla_inicio,text="Centro Multimedia FSE")
	titulo.pack()
	
	#Crea botón que llama al menu principal y se envia la ventana actual.
	im_inicio=PhotoImage(file='bienvenido_logo.png')
	boton_inicio=Button(pantalla_inicio,image=im_inicio,command=lambda:menu(pantalla_inicio))
	boton_inicio.place(x=200,y=500)  

	pantalla_inicio.mainloop()
