from constants import *
from graph import X, O

import pygame


class Button:
    def __init__(self, label, x, y, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=WHITE,  visible=True) -> None:
        self.label = label
        self.x = x
        self.y = y
        self.width, self.height = width, height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = color
        self.visible = visible

    def draw(self, window) -> None:
        if self.visible:
            pygame.draw.rect(window, self.color, self.rect, border_radius=10)
            current_font = pygame.font.SysFont(FONT, BUTTON_FONT_SIZE)
            label = current_font.render(self.label, True, BUTTON_FONT_COLOR)
            label_rect = label.get_rect(
                center=(self.x + self.width // 2, self.y + self.height // 2))
            window.blit(label, label_rect)

    def clicked(self, pos) -> bool:
        return self.visible and self.rect.collidepoint(pos)

    def select(self) -> None:
        self.color = BLUE

    def unselect(self) -> None:
        self.color = WHITE


def initialize_buttons() -> dict[int | str, Button]:
    buttons = {}

    x = (WINDOW_WIDTH - BUTTON_WIDTH) // 2
    y = WINDOW_HEIGHT // 6 - 50

    buttons[X] = Button("Play as X", x-0.75*BUTTON_WIDTH, y)
    buttons[O] = Button("Play as O", x+0.75*BUTTON_WIDTH, y)

    return buttons
