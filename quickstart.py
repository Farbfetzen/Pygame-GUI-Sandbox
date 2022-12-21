"""An implementation of the quickstart example.
See https://pygame-gui.readthedocs.io/en/latest/quick_start.html
"""

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
import pygame_gui


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = "#123456"

pygame.init()
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Pygame-GUI-Sandbox")
clock = pygame.time.Clock()
is_running = True

gui_manager = pygame_gui.UIManager((CANVAS_WIDTH, CANVAS_HEIGHT))
hello_button_rect = pygame.Rect(0, 0, 100, 50)
hello_button_rect.center = canvas.get_rect().center
hello_button = pygame_gui.elements.UIButton(
    relative_rect=hello_button_rect,
    text="Say Hello",
    manager=gui_manager
)

while is_running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print("Hello, world!")
        gui_manager.process_events(event)

    gui_manager.update(dt)

    canvas.fill(BACKGROUND_COLOR)
    gui_manager.draw_ui(canvas)
    pygame.display.flip()
