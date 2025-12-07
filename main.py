mport pygame
import sys
from tower import Tower
from enemy import Enemy
from map import Map

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

# Game variables
map_grid = Map()
towers = []
enemies = []
enemy_spawn_timer = 0
level = 1
lives = 10
money = 100
score = 0

# Basic game loop
running = True
while running:
    screen.fill((50,50,50))  # background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Place tower on click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if money >= 50 and map_grid.is_valid_tile(x, y):
                towers.append(Tower(x, y))
                money -= 50

    # Spawn enemies
    enemy_spawn_timer += 1
    if enemy_spawn_timer > 120:  # spawn every 2 seconds
        enemies.append(Enemy(path=map_grid.path))
        enemy_spawn_timer = 0

    # Update enemies
    for enemy in enemies[:]:
        enemy.move()
        if enemy.reached_end():
            lives -= 1
            enemies.remove(enemy)
        elif enemy.health <= 0:
            enemies.remove(enemy)
            score += 10
            money += 20

    # Update towers
    for tower in towers:
        tower.update(enemies)

    # Draw map
    map_grid.draw(screen)

    # Draw towers
    for tower in towers:
        tower.draw(screen)

    # Draw enemies
    for enemy in enemies:
        enemy.draw(screen)

    # HUD
    font = pygame.font.SysFont(None, 30)
    hud = font.render(f"Lives: {lives}  Money: {money}  Score: {score}  Level: {level}", True, (255,255,255))
    screen.blit(hud, (10,10))

    pygame.display.flip()
    clock.tick(60)

    # Game over
    if lives <= 0:
        print("Game Over! Score:", score)
        running = False

pygame.quit()
sys.exit()
