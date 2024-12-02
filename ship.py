class Ship:


    def __init__(self, x: int, y: int, name: str) -> None:
        """
        Initialize a ship object with given coordinates and name.

        There are 4 attributes of the ship:
        x (int): The x coordinate of the ship.
        y (int): The y coordinate of the ship.
        name (str): The name or type of the ship.
        sunk (bool): Indicates whether the ship has sunk.
        """

        self.__x = x
        self.__y = y
        self.__name = name
        self.__sunk = False

    def set_sunk(self):
        """
        Update the status of the ship when it gets hit.
        If the ship is hit, it is marked as sunk.
        """

        self.__sunk = True

    def get_sunk(self) -> bool:
        """Get the status of the ship."""

        return self.__sunk

    def get_name(self) -> str:
        """Get the name of the ship."""

        return self.__name

    def get_coord(self) -> tuple[int , int]:
        """Get the coordinate of the ship."""

        return self.__x, self.__y

    def __repr__(self) -> str:
        """
        Returns a formatted string representation of the ship.

        The formatted string includes the ship's name followed by its status:
        - If the ship has sunk, the format is "{name}: Sunk".
        - If the ship hasn't sunk, the format is "{name}: Afloat".
        """

        return f"{self.__name}: {"Sunk" if self.__sunk else "Afloat"}"

    @staticmethod
    def create_ships() -> list["Ship"]:
        """
        Creates a list of ships and returns it.

        Currently, the implementation returns a static list of ships.
        You will need to change it so the ships are created by the
        user through inputs.
        """

        ships = []
        print("Creating ships...")

        while len(ships) < 10:
            user_input = input("> ")

            if user_input == "END SHIPS":
                break

            try:
                name, x, y = user_input.split(" ")
            except ValueError:
                print("Error: <symbol> <x> <y>")
                continue

            if name == "" or y == "":
                print("Error: <symbol> <x> <y>")
                continue

            if not "A" <= name < "K":
                print("Error: symbol must be between 'A'-'J'")

            elif not (x.lstrip('-').isdigit() or y.lstrip('-').isdigit()):
                print(f"Error: ({x}, {y}) is an invalid coordinate")

            elif not (int(x) in range(5) and int(y) in range(5)):
                print(f"Error: ({x}, {y}) is out-of-bound on 5x5 board")

            elif any(ship.get_coord() == (int(x), int(y)) for ship in ships):
                print(f"Error: ({x}, {y}) is already occupied by Ship{next(ship.__name for ship in ships if ship.get_coord() == (int(x), int(y)))}")

            elif any(ship.get_name() == name for ship in ships):
                print(f"Error: symbol '{name}' is already token")

            else:
                ships.append(Ship(int(x), int(y), name))
                print(f"Success! Ship{name} added at ({x}, {y})")

        print(f"{len(ships)} ships added.")
        return ships
