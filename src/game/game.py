"""Main application coordinator for Macheteando."""

import json
from pathlib import Path

import pygame

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "game.example.json"
DEFAULT_SCREEN_WIDTH = 1280
DEFAULT_SCREEN_HEIGHT = 720
DEFAULT_FPS = 60


class Game:
    """Owns application initialization and the main loop.

    The ECS World (spec 001) and the Scene Manager (spec 010) are
    integration points declared here but intentionally left
    unconnected until their own specifications are implemented.
    """

    def __init__(self) -> None:
        pygame.init()

        config = self._load_config()
        screen_config = config.get("screen", {})
        width = int(screen_config.get("width", DEFAULT_SCREEN_WIDTH))
        height = int(screen_config.get("height", DEFAULT_SCREEN_HEIGHT))
        self.fps = int(screen_config.get("fps", DEFAULT_FPS))

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Macheteando")
        self.clock = pygame.time.Clock()

        self.running = True

        # R7: integration points connected by their own specifications.
        self.world = None  # ECS World -> spec 001
        self.scene_manager = None  # SceneManager -> spec 010

    @staticmethod
    def _load_config() -> dict:
        """Read external configuration, falling back to safe defaults."""
        try:
            with CONFIG_PATH.open(encoding="utf-8") as config_file:
                return json.load(config_file)
        except (OSError, ValueError):
            return {}

    def run(self) -> None:
        """Run the application until a quit event is received.

        Detailed scene, ECS and gameplay behavior will be implemented
        by their corresponding specifications.
        """
        try:
            while self.running:
                self._handle_events()
                self._update()
                self._render()
                self.clock.tick(self.fps)
        finally:
            self.quit()

    def _handle_events(self) -> None:
        """Capture application events (game input arrives in spec 003)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self) -> None:
        """Update systems and scenes (specs 001+ and 010)."""

    def _render(self) -> None:
        """Draw the current state (RenderSystem arrives in spec 010)."""
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def quit(self) -> None:
        """Shut down Pygame and release application resources."""
        pygame.quit()
