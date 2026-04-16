"""Module for Tic-Tac-Toe game."""


import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def draw_board(board: list[str]) -> None:
    logger.info("\n %s | %s | %s ", board[0], board[1], board[2])
    logger.info("-----------")
    logger.info(" %s | %s | %s ", board[3], board[4], board[5])
    logger.info("-----------")
    logger.info(" %s | %s | %s ", board[6], board[7], board[8])


def check_victory(board: list[str]) -> bool:
    win_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for x, y, z in win_lines:
        if board[x] == board[y] == board[z] != " ":
            return True
    return False


def start_game() -> None:
    board: list[str] = [" "] * 9
    player_num: int = 1
    symbol: str = "X"

    logger.info("Welcome to Tic-Tac-Toe!")

    for _ in range(9):
        draw_board(board)

        while True:
            logger.info("Player %s (%s), it's your turn.", player_num, symbol)
            try:
                choice: int = int(input("Choose a cell (0-8): "))
                if board[choice] != " ":
                    logger.info("This cell is already taken! Try again.")
                    continue

                board[choice] = symbol
                break
            except (ValueError, IndexError):
                logger.info("Invalid input! Please enter a number from 0 to 8.")

        if check_victory(board):
            draw_board(board)
            logger.info("Congratulations! Player %s wins!", player_num)
            return
        if player_num == 1:
            player_num = 2
            symbol = "O"
        else:
            player_num = 1
            symbol = "X"

    draw_board(board)
    logger.info("It's a draw! No more moves left.")


if __name__ == "__main__":
    start_game()
