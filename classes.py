import pygame, math

class Bob:
    def __init__(self, x, y):
        self.radius = 150
        self.x = x
        self.y = y
        self.x_speed, self.y_speed = 0, 0
    def update_on_screen(self, screen):
        self.x += self.x_speed
        self.y += self.y_speed
        pygame.draw.circle(screen, (145, 86, 56), (self.x, self.y), self.radius)
        pygame.draw.circle(screen, (100, 41, 11), (self.x, self.y), self.radius/2)
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius/10)
        pygame.draw.arc(
    screen,
    (0, 0, 255),
    pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2),
    math.pi,
    0,
    300
)

class Spring:
    def __init__(self, a, b):
        self.rest_lenght = 50
        self.start_pos, self.end_pos = a, b
        self.k = 0.1
    def update_pos(self, a, b):
        self.start_pos, self.end_pos = a, b
    def get_x(self):
        dx = self.end_pos[0] - self.start_pos[0]
        dy = self.end_pos[1] - self.start_pos[1]
        dist = math.hypot(dx, dy)
        nx = dx / dist
        ny = dy / dist
        return [nx, ny]
    def get_force(self):
        dx = self.end_pos[0] - self.start_pos[0]
        dy = self.end_pos[1] - self.start_pos[1]
        dist = math.hypot(dx, dy)
        if dist == 0:
            return 0, 0
        nx = dx / dist
        ny = dy / dist
        force_magnitude = self.k * (dist - self.rest_lenght)
        fx = nx * force_magnitude
        fy = ny * force_magnitude
        return fx, fy 
import script