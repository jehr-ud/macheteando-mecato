"""Application entry point for Macheteando.

The entry point is intentionally small. It is responsible only for
bootstrapping the application and delegating execution to the game layer.

Gameplay rules, ECS systems, entity creation and rendering must not be
implemented in this file.
"""

from src.game.game import Game


def main() -> None:
    """Create and run the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
