import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)

# Tamaño de la ventana
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake en Python")

# Reloj y tamaño del bloque
clock = pygame.time.Clock()
tam_bloque = 20
velocidad = 10

# Fuente para el puntaje
fuente = pygame.font.SysFont("Arial", 25)

# Mostrar puntaje
def mostrar_puntaje(puntaje):
    valor = fuente.render("Puntos: " + str(puntaje), True, negro)
    pantalla.blit(valor, [0, 0])

# Juego principal
def juego():
    game_over = False
    game_close = False

    # Posición inicial
    x = ancho // 2
    y = alto // 2
    x_cambio = 0
    y_cambio = 0

    cuerpo_serpiente = []
    largo_serpiente = 1

    # Comida aleatoria
    comida_x = round(random.randrange(0, ancho - tam_bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto - tam_bloque) / 20.0) * 20.0

    while not game_over:
        while game_close:
            pantalla.fill(blanco)
            mensaje = fuente.render("¡Perdiste! C para continuar o Q para salir", True, rojo)
            pantalla.blit(mensaje, [ancho / 6, alto / 3])
            mostrar_puntaje(largo_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        # Movimiento
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cambio = -tam_bloque
                    y_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cambio = tam_bloque
                    y_cambio = 0
                elif evento.key == pygame.K_UP:
                    y_cambio = -tam_bloque
                    x_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y_cambio = tam_bloque
                    x_cambio = 0

        # Ver límites
        if x >= ancho or x < 0 or y >= alto or y < 0:
            game_close = True

        x += x_cambio
        y += y_cambio
        pantalla.fill(blanco)

        # Dibujar comida
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tam_bloque, tam_bloque])

        # Dibujar serpiente
        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        cuerpo_serpiente.append(cabeza)

        if len(cuerpo_serpiente) > largo_serpiente:
            del cuerpo_serpiente[0]

        # Ver colisiones
        for bloque in cuerpo_serpiente[:-1]:
            if bloque == cabeza:
                game_close = True

        for parte in cuerpo_serpiente:
            pygame.draw.rect(pantalla, negro, [parte[0], parte[1], tam_bloque, tam_bloque])

        mostrar_puntaje(largo_serpiente - 1)

        pygame.display.update()

        # Comer comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ancho - tam_bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto - tam_bloque) / 20.0) * 20.0
            largo_serpiente += 1

        clock.tick(velocidad)

    pygame.quit()
    quit()

# Ejecutar juego
juego()
