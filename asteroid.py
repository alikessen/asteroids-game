from circleshape import CircleShape
import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # if it's already the smallest size, nothing to do
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # split into two smaller asteroids
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_vector1 = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        ast1.velocity = new_vector1 * 1.2
        ast2.velocity = new_vector2 * 1.2
