from ship import Ship


def create_board() -> list[list[Ship | None]]:
    """
    Create a 2D list representing the game board. The size will be
    5x5 with all slots set to None.
    """

    return [[None for _ in range(5)] for _ in range(5)]


def print_board(board: list[list[Ship | None]]) -> None:
    """
    Prints the game board with the ships.
    You can assume the board is 5x5.
    """

    print("-------")
    for row in board: print("|" + "".join(" " if not cell else "X" if cell.get_sunk() else cell.get_name() for cell in row) + "|")
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
    if len(ships) == 0:
        return print("No ships.")

    # 2. Create the 5x5 board
    board = create_board()

    # 3. Place your ships in the board based on their coordinates
    for ship in ships:
        x, y = ship.get_coord()
        board[x][y] = ship

    # 4. Continuously prompt the user for input until all ships are sunk.
    #    Whenever a ship is sunk, update the ship's status accordingly.
    print("Game started. Fire at will!")
    for i in range(10):

        print_board(board)

        try:
            x, y = map(int, input(f"Enter X, Y coordinate [{i + 1}/10]: ").split(", "))
        except ValueError:
            print("Invalid coordinates. Try again.")
            continue

        if not (x in range(5) and y in range(5)):
            print("Invalid coordinates. Try again.")
        elif not board[x][y]:
            print("Miss!")
        elif board[x][y].get_sunk():
            print(f"Ship {board[x][y].get_name()} is already sunk!")
        else:
            board[x][y].set_sunk()
            print(f"You sank Ship {board[x][y].get_name()}!")
            if is_finished(board):
                print_board(board)
                print("Congratulations! All ships are sunk!")
                break

    if not is_finished(board):
        print("Game over! You've used all 10 attempts.")


if __name__ == "__main__":
    main()
