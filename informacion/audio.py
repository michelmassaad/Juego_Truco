import pygame as pg
from funciones.complementarias import resource_path

# Cargar la música de fondo
sonido_barajear = pg.mixer.Sound(resource_path("audio/sonido_lanzar_carta.wav"))
sonido_lanzar_carta = pg.mixer.Sound(resource_path("audio/sonido_lanzar_carta.wav"))

# Ajustar el volumen de la música
pg.mixer.music.set_volume(0.3)  # Volumen de 0.0 a 1.0