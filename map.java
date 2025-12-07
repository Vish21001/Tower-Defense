import pygame

class Map:
    def __init__(self):
        # Simple path for enemies
        self.path = [(50,550),(50,300),(300,300),(300,100),(700,100),(700,500)]
        self.tiles = []  # Optional: grid for tower placement

    def is_valid_tile(self, x, y):
        # Simple check: don't place towers on path
        for px, py in self.path:
            if abs(x - px) < 30 and abs(y - py) <30:
                return False
        return True

    def draw(self, screen):
        # Draw path
        for i in range(len(self.path)-1):
            pygame.draw.line(screen, (100,100,100), self.path[i], self.path[i+1], 20)
