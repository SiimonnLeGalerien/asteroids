import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    font = pygame.font.SysFont('arial', 32)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for upt in updatable:
            upt.update(dt)
        for ast in asteroids:
            if player.collides(ast):
                print("Game Over!")
                return
            for shot in shots:
                if ast.collides(shot):
                    player.score += ast.split()
                    print(player.score)
                    shot.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        score = font.render(f"SCORE: {player.score}", False, (255, 255, 255))
        screen.blit(score, (20, 690))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
