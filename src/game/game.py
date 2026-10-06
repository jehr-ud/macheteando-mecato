"""Main application coordinator for Macheteando."""

import pygame


class Game:
    """Owns application initialization and the main loop."""

    def __init__(self) -> None:
        pygame.init()
        self.running = True

    def run(self) -> None:
        """Run the application.

        Detailed scene, ECS and gameplay behavior will be implemented
        by their corresponding specifications.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()
