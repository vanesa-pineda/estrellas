import pygame
import random

# Configuración de la ventana
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Atrapa las Estrellas")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Personaje
player = pygame.Rect(375, 500, 50, 50)

# Estrellas
stars = [pygame.Rect(random.randint(0, 750), random.randint(-100, -10), 20, 20) for _ in range(5)]

# Reloj
clock = pygame.time.Clock()

# Puntuación
score = 0

# Bucle principal
running = True
while running:
    screen.fill(BLACK)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < 800:
        player.x += 5
    
    # Movimiento de las estrellas
    for star in stars:
        star.y += 5
        if star.y > 600:
            star.y = random.randint(-100, -10)
            star.x = random.randint(0, 750)
        
        # Colisión con el jugador
        if player.colliderect(star):
            score += 1
            star.y = random.randint(-100, -10)
            star.x = random.randint(0, 750)
    
    # Dibujar elementos
    pygame.draw.rect(screen, WHITE, player)
    for star in stars:
        pygame.draw.circle(screen, YELLOW, star.center, 10)
    
    # Mostrar puntuación
    font = pygame.font.SysFont('Arial', 24)
    text = font.render(f'Puntuación: {score}', True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
