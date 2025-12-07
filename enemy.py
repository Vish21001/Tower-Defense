import pygame

class Enemy:
    def __init__(self, path):
        self.path = path
        self.x, self.y = path[0]
        self.index = 0
        self.speed = 1
        self.health = 50

    def move(self):
        if self.index < len(self.path)-1:
            target_x, target_y = self.path[self.index+1]
            dx = target_x - self.x
            dy = target_y - self.y
            dist = (dx**2 + dy**2)**0.5
            if dist != 0:
                self.x += self.speed * dx/dist
                self.y += self.speed * dy/dist
            if abs(self.x - target_x) < 1 and abs(self.y - target_y) <1:
                self.index += 1

    def reached_end(self):
        return self.index >= len(self.path)-1

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x-10, self.y-10, 20,20))
        # Health bar
        pygame.draw.rect(screen, (0,255,0), (self.x-10, self.y-15, 20*(self.health/50), 3))
