import multiprocessing
import tkinter
import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pygame

from tetris_oficial import Tetris
from Detector_Dedos import Reconocimiento
from ProyectoSnake.Snake import Snake
from Mario.mario_level_1 import mario



def start_game(game_func, root, game):
    def wrapper():
        # Detener la música
        pygame.mixer.music.stop()
        # Cerrar la ventana del menú
        root.destroy()
        # Iniciar el juego y el reconocimiento de dedos
        p1 = multiprocessing.Process(target=Reconocimiento, args=(game,))
        p2 = multiprocessing.Process(target=game_func)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    return wrapper

def create_menu(root):
    root.title("Menu de Juegos")
    root.geometry("600x500")

    # Crear una lista con todos los frames del GIF
    gif = Image.open("D:\\Ingenieria en Sistemas\\7 semestre\\inteligencia artificial\\proyectofinal\\Proyecto\\assets\\Arcade1.gif")
    frames = []
    for i in range(gif.n_frames):
        gif.seek(i)
        frame = ImageTk.PhotoImage(gif)
        frames.append(frame)

    # Cargar el último frame del GIF
    ultimo_frame = frames[8]

    # Crear un label que mostrará el GIF
    gif_label = tk.Label(root, image=ultimo_frame)
    gif_label.place(relx=0.5, rely=0.5, anchor="center") # Centrar el label en la ventana

    # Función que se ejecutará para animar el GIF
    def animar(frame):
        gif_label.configure(image=frame)
        if frame == ultimo_frame:
            pass # El GIF ha terminado de animarse
            # Crear los botones del menú
            font=customtkinter.CTkFont(family='MegaMan 2', size=20)

            tetriz_button = customtkinter.CTkButton(master=root, text="TETRIS", command=start_game(Tetris, root, 'TETRIS'), width=250, height=50, border_width=3,corner_radius=0,fg_color='#a31119', hover_color='#ff0000', border_color='#000000', font=font)
            tetriz_button.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER) # Colocar el botón en el centro de la parte superior de la ventana
         
            serpiente_button = customtkinter.CTkButton(master=root, text="Mario BROS", command=start_game(mario, root, 'MARIO'), width=250, height=50, border_width=3,corner_radius=0,fg_color='#a31119', hover_color='#ff0000', border_color='#000000', font=font)
            serpiente_button.place(relx=0.5, rely=0.50, anchor=tkinter.CENTER) # Colocar el botón en el centro de la ventana

            nave_button = customtkinter.CTkButton(master=root, text="SNAKE", command=start_game(Snake, root, 'SNAKE'), width=250, height=50, border_width=3,corner_radius=0,fg_color='#a31119',hover_color='#ff0000', border_color='#000000', font=font)
            nave_button.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER) # Colocar el botón en el centro de la parte inferior de la ventana
        else:
            root.after(100, animar, frames[frames.index(frame) + 1])
    
    # Comenzar a animar el GIF desde el primer frame
    gif_label.configure(image=frames[0])
    animar(frames[0])

def play_music():
    # Inicializar pygame
    pygame.init()
    # Cargar la música en un objeto pygame.mixer.music
    #pygame.mixer.music.load("Music/Menu.mp3")
    # Reproducir la música en bucle infinito y ajustar volumen
    #pygame.mixer.music.set_volume(0.1)
    #pygame.mixer.music.play(-1) 
    

def main():
    play_music()
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    # Crear la instancia de Tk
    root = customtkinter.CTk()
    # Crear la ventana del menú
    create_menu(root)
    # Iniciar el bucle de eventos
    root.mainloop()

if __name__ == "__main__":
    main()
