from ship import Ship


def create_board() -> list[list[Ship | None]]:
    """
    Create a 2D list representing the game board. The size will be
    5x5 with all slots set to None.
    """

    board = [
        [None] * 5,
        [None] * 5,
        [None] * 5,
        [None] * 5,
        [None] * 5
    ]
    return board


def print_board(board: list[list[Ship | None]]) -> None:
    """
    Prints the game board with the ships.
    You can assume the board is 5x5.
    """

    print("-------")
    for x in range(5):
        print("|", end="")
        for y in range(5):
            if board[x][y] is None:
                print(" ", end="")
            elif board[x][y].sunk:
                print("X", end="")
            else:
                print(board[x][y].get_name(), end="")
        print("|")
    print("-------")


# you will need to modify the implementation of this function
def is_finished(board: list[list[Ship | None]]):
    """
    Check if all ships on the 2D list game board are sunk.
    Returns True if all ships are sunk, otherwise False.
    """

    return all(ship.get_sunk() for row in board for ship in row if ship)


def main():
    """Runs the game."""
    # 1. Create the list of ships
    ships = Ship.create_ships()

    # 2. Create the 5x5 board
    board = create_board()

    # 3. Place your ships in the board based on their coordinates
    for ship in ships:
        x, y = ship.get_coord()
        board[y][x] = ship

    # 4. Continuously prompt the user for input until all ships are sunk.
    #    Whenever a ship is sunk, update the ship's status accordingly.
    print("Game started. Fire at will!")
    for i in range(1, 11):
        print_board(board)

        try:
            x, y = map(int, input(f"Enter X, y coordinate [{i}/10]: ").split())
        except ValueError:
            print("Invalid coordinates. Try again.")
            continue

        if not (x in range(5) and y in range(5)):
            print("Invalid coordinates. out-of-bound on 5x5 board. Try again.")
            continue

        if board[x][y] is None:
            print("Miss!")
            continue

        if board[x][y].get_sunk():
            print(f"Ship {board[x][y].get_name()} is already sunk!")
        else:
            board[x][y].set_sunk()
            print(f"You sank Ship{board[x][y].get_name()}!")

        if is_finished(board):
            print("Congratulations! All ships are sunk!")
            break

    if not is_finished(board):
        print("Game over! You've used all 10 attempts.")


if __name__ == "__main__":
    main()


