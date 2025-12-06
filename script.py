import pygame, random
from classes import *

pygame.init()
w, h = 600, 600
screen = pygame.display.set_mode((w, h))
running = True
top_color = (44, 0, 163)
gravity = 4
bob = Bob(150, 350)
bob2 = Bob(w-150, 350)
anchor = Bob(150, 15)
anchor2 = Bob(w-150, 15)
spring = Spring((bob.x, bob.y), (anchor.x, anchor.y))
spring2 = Spring((bob2.x, bob2.y), (anchor2.x, anchor2.y))
clock = pygame.time.Clock()
tping = False
anchor_g_up = False
def move_anchor():
    global anchor_g_up, anchor
    min_y, max_y = 150, 300
    anchor_speed = 10

    if anchor_g_up:
        anchor.y += anchor_speed
        if anchor.y >= max_y:
            anchor_g_up = False
    else:
        anchor.y -= anchor_speed
        if anchor.y <= min_y:
            anchor_g_up = True

def draw_filled_arc(screen, x, y, radius, color, steps=100):
    points = [(x, y)]  # centro do círculo
    for i in range(steps + 1):
        # angulo de π (esquerda) até 0 (direita)
        angle = math.pi * (1 - i / steps)  # vai de π → 0
        px = x + radius * math.cos(angle)
        py = y + radius * math.sin(angle)  # positivo y cresce para baixo no Pygame
        points.append((px, py))

    pygame.draw.polygon(screen, color, points)

while running:
    clock.tick(60)
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            tping = True
        if event.type == pygame.MOUSEBUTTONUP:
            tping = False
    keys = pygame.key.get_pressed()

    move_anchor()
    anchor2.y = anchor.y + random.randint(-100, 100)
    #spring 1
    spring.update_pos((bob.x, bob.y), (anchor.x, anchor.y))

    #spring 2
    spring2.update_pos((bob2.x, bob2.y), (anchor2.x, anchor2.y))
    
    #bob1
    bob.update_on_screen(screen)
    bob.y_speed += spring.get_force()[1]
    bob.x_speed += spring.get_force()[0]
    bob.y_speed += gravity
    bob.y_speed *= 0.8
    bob.x_speed *= 0.8
    #bob2
    bob2.update_on_screen(screen)
    bob2.y_speed += spring2.get_force()[1]
    bob2.x_speed += spring2.get_force()[0]
    bob2.y_speed += gravity
    bob2.y_speed *= 0.8
    bob2.x_speed *= 0.8
    draw_filled_arc(screen, bob.x, bob.y, bob.radius, top_color)
    draw_filled_arc(screen, bob2.x, bob2.y, bob2.radius, top_color)
    pygame.display.flip()

pygame.quit()
