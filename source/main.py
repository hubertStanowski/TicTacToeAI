from constants import *
from graph import *
from buttons import initialize_buttons
from tictactoe import *

import pygame


def main() -> None:
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("TicTacToe AI")

    clock = pygame.time.Clock()
    game = TicTacToe(GRID_SIZE)
    human_player = None
    buttons = initialize_buttons()

    while True:
        turn = game.player()
        clock.tick(FPS)
        window.fill(BACKGROUND_COLOR)

        if human_player:
            game.graph.draw(window)
            if game.terminal():
                display_result(window, game)
        else:
            for button in buttons.values():
                button.draw(window)

        # AI Move
        if human_player:
            if turn != human_player and not game.terminal():
                pygame.display.update()
                pygame.time.delay(500)
                move = game.minimax()
                game = game.result(move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if not human_player:
                    for label, button in buttons.items():
                        if button.clicked(pos):
                            human_player = label
                else:
                    col, row = game.graph.get_grid_pos(pos)
                    if (row, col) in game.actions() and not game.terminal():
                        game.graph.grid[row][col] = turn
            elif event.type == pygame.KEYDOWN:
                game.reset()
                human_player = None

        pygame.display.update()


def display_result(window, game) -> None:
    if not game.winner():
        text = "Draw"
    else:
        text = "AI won!"

    font = pygame.font.SysFont(FONT, RESULT_FONT_SIZE)
    label = font.render(text, True, WHITE)
    label_rect = label.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 6))

    window.blit(label, label_rect)


if __name__ == "__main__":
    main()
