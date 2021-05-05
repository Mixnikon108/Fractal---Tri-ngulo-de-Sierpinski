import pygame
import time    

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CAFE = (90, 50, 15)
AMARILLO = (255, 255, 0)
VERDE = (100, 240, 0)


pygame.init()
Dimensiones = (700, 700)
Pantalla = pygame.display.set_mode(Dimensiones)
pygame.display.set_caption("Introducción a los Gráficos")
reloj = pygame.time.Clock()
Pantalla.fill(BLANCO)

def midpoint(A, B):
	return (A[0] + B[0])/2, (A[1] + B[1])/2
def dibujar(triangulo):
	pygame.draw.polygon(Pantalla, ROJO, [triangulo[0],triangulo[1], triangulo[2]], 1)
	pygame.display.flip()

A = (100, 100)
B = (500, 100)
C = (300, 450)

triangulo = (A, B, C)

lista  = []
def fun(depth, triangulo):
	
	Mab = midpoint(triangulo[0], triangulo[1])
	Mac = midpoint(triangulo[0], triangulo[2])
	Mbc = midpoint(triangulo[1], triangulo[2])

	triangulo_1 = (triangulo[0], Mab, Mac)
	triangulo_2 = (triangulo[1], Mab, Mbc)
	triangulo_3 = (triangulo[2], Mbc, Mac)
	#triangulo_4 = (Mbc, Mab, Mac)

	if depth <= 0:
		dibujar(triangulo_1)
		dibujar(triangulo_2)
		dibujar(triangulo_3)
		#dibujar(triangulo_4)
		
	else:
		fun(depth - 1, triangulo_1)
		fun(depth - 1, triangulo_2)
		fun(depth - 1, triangulo_3)
		#fun(depth - 1, triangulo_4)



fun(5, triangulo)
time.sleep(5)
