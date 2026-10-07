"""Smoke tests for the application bootstrap (spec 000).

These tests run Pygame headlessly using dummy SDL drivers so they can
execute in environments without a display or audio device.
"""

import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame  # noqa: E402  (must follow the SDL environment setup)

import main  # noqa: E402
from src.game.game import Game  # noqa: E402


def test_main_exposes_main_function() -> None:
    assert callable(main.main)


def test_game_declares_integration_points() -> None:
    game = Game()
    try:
        # R7: ready to be connected by specs 001 (ECS) and 010 (scenes).
        assert game.world is None
        assert game.scene_manager is None
        assert game.fps > 0
        assert game.screen.get_size() == (1280, 720)
    finally:
        game.quit()


def test_run_starts_and_shuts_down_cleanly() -> None:
    game = Game()

    # A quit event posted before the loop makes the run terminate
    # deterministically while still exercising a full frame.
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    game.run()

    assert game.running is False
    # pygame.quit() must have been executed by run().
    assert not pygame.get_init()
