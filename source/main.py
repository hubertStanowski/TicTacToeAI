from constants import *
from graph import *
from buttons import initialize_buttons
from tictactoe import *

import pygame

# TODO add buttons to select which player is human
# TODO and then start the game against ai


def main() -> None:
    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("TicTacToe AI")

    clock = pygame.time.Clock()
    game = TicTacToe(GRID_SIZES["small"])
    buttons = initialize_buttons()
    cooldown = CLICK_COOLDOWN

    while True:
        turn = game.player()
        cooldown += 1
        clock.tick(FPS)
        window.fill(BACKGROUND_COLOR)
        for button in buttons.values():
            button.draw(window)

        game.graph.draw(window)
        if game.terminal():
            display_result(window, game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                for label, button in buttons.items():
                    if button.clicked(pos):
                        button.select()
                col, row = game.graph.get_grid_pos(pos)

                if game.graph.is_valid_node(row, col) and cooldown >= CLICK_COOLDOWN and not game.terminal():
                    cooldown = 0
                    if game.graph.is_empty(row, col):
                        if turn == X:
                            game.graph.set_x(row, col)
                        else:
                            game.graph.set_o(row, col)
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE):
                game.reset()

        pygame.display.update()


def display_result(window, game) -> None:
    winner = game.winner()
    if not winner:
        text = "Draw"
    else:
        text = f"{winner} won!"

    font = pygame.font.SysFont(FONT, RESULT_FONT_SIZE)
    label = font.render(text, True, WHITE)
    label_rect = label.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 5))

    window.blit(label, label_rect)


# def display_reset(window: pygame.Surface) -> None:
#     font = pygame.font.SysFont(FONT, RESET_FONT_SIZE)
#     label = font.render("RESET", True, RED)
#     label_rect = label.get_rect(
#         center=((2*LEFT_MARGIN + GAME_SIZE) // 2, WINDOW_HEIGHT // 2.3))

#     window.blit(label, label_rect)
#     pygame.display.update()
#     pygame.time.delay(1000)


if __name__ == "__main__":
    main()
