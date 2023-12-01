from random import choice

from observers import Subject


class GameEngine(Subject):
    """
    Die Game Engine kapselt die Spiellogik, sowie den Ablauf des Spiels von der Initialisierung bis hin zur Entscheidung
    wann das Spiel vorbei ist.
    """

    def __init__(self):
        super().__init__()
        # self.grid ist das Abbild des Spielfelds für die Berechnungen
        self.grid = []
        # self.tiles ist von gleicher Dimension wie `grid` wird jedoch zur Speicherung der Kacheln genutzt.
        self.tiles = []
        self.game_over = False

    def reset_game(self):
        """
        Setzt das Spielfeld und den Punktestand zurück. Erzeugt ein neues, zufälliges `grid` und setzt den
        Spielstand zurück
        """
        self.game_over = False
        self.grid = None
        self.tiles = []
        self.start_game(4)
        self.notify({"resetScore": True})

    def render(self):
        pass

    @staticmethod
    def setup_grid(grid_size):
        """
        Erstellt ein neues Spielfeld der gewünschten Größe. Dafür wird List Comprehension verwendet.
        Vgl. https://www.w3schools.com/python/python_lists_comprehension.asp
        """
        return [[0 for x in range(grid_size)] for y in range(grid_size)]

    def start_game(self, grid_size):
        """
        Erstellt ein `grid` mit der gewünschten Größe und platziert eine 2 an zufälliger Stelle darauf.
        """
        self.grid = self.setup_grid(grid_size)
        self.add_random_tile(self.grid, 2)

    def update(self, direction: str):
        """
        Die Update-Methode kapselt die Aktualisierung der Spielfeldmatrix je nach Richtung. Im Spielfeld
        muss zunächst überprüft werden, ob aktualisiert werden darf. Dann speichern wir den aktuellen Stand zwischen
        und aktualisieren das Spielfeld.
        """

        if self.should_update():
            current_grid = self.grid

            if direction == "left":
                self.grid = self.update_grid_to_left(self.grid)
            elif direction == "right":
                self.grid = self.update_grid_to_right(self.grid)
            elif direction == "down":
                self.grid = self.update_grid_to_down(self.grid)
            elif direction == "up":
                self.grid = self.update_grid_to_up(self.grid)

            # es wird nur eine neue Zahl hinzugefügt, wenn sich das Spielfeld verändert hat
            if self.grid != current_grid:
                self.add_random_tile(self.grid)
        else:
            self.game_over = True

    def update_grid_to_left(self, grid):
        updated_grid = []

        for row in grid:
            updated_row = self.update_row_to_left(row)
            updated_grid.append(updated_row)

        return updated_grid

    def update_grid_to_right(self, grid):
        updated_grid = []

        for row in grid:
            updated_row = self.update_row_to_right(row)
            updated_grid.append(updated_row)

        return updated_grid

    def update_row_to_left(self, row, start_index=0):
        """
        Aktualisiert eine Zeile von links nach rechts: Sind zwei benachbarte Elemente identisch wird das
        linke verdoppelt und das rechte entfernt.
        """
        for i in range(start_index, len(row) - 1):
            if row[i] == row[i + 1] and row[i] > 0:
                row[i] = row[i] * 2

                payload = {"latestScore": row[i]}
                self.notify(payload)
                row.pop(i + 1)
                # Damit die Felddimensionen erhalten bleiben wird eine 0 hinten angefügt
                row.append(int(0))

                return self.update_row_to_left(row, i + 1)

            # verhindert, dass eine 0 am Anfang der Zeile stehen bleibt
            elif row[i] == row[i + 1] and row[i] == 0:
                continue

            # entfernt Felder mit 0 die nicht am Ende der Zeile sind (verhindert endlose Rekursion)
            elif row[i] == 0 and i != len(row) - 1:
                row.pop(i)
                row.append(int(0))
                return self.update_row_to_left(row, start_index)
            else:
                continue

        return row

    def update_row_to_right(self, row):

        reversed_row = row[::-1]
        updated_reversed_row = self.update_row_to_left(reversed_row)

        updated_row = updated_reversed_row[::-1]

        return updated_row

    @staticmethod
    def row_vector_from_matrix(matrix: list, vector_column: int):
        """
        Erstellt einen Reihenvektor
        """
        vector = []
        for row in matrix:
            vector.append(row[vector_column])

        return vector

    @staticmethod
    def transpose_grid(grid):
        """
        Quelle: https://stackoverflow.com/questions/10169919/python-matrix-transpose-and-zip
        Funktion zum transponieren einer Matrix (macht aus Zeilen Spalten und umgekehrt)
        """
        return list(map(list, zip(*grid)))

    def update_grid_to_down(self, grid):
        """
        Die Ausgangsmatrix wird transponiert und dann in die update_row_to_right Methode übergeben.
        Das Ergebnis wird wieder transponiert und ist das korrekte Ergebnis für die Bewegung nach unten.
        """
        transposed_grid = self.transpose_grid(grid)
        updated_transposed_grid = self.update_grid_to_right(transposed_grid)
        updated_grid = self.transpose_grid(updated_transposed_grid)

        return updated_grid

    def update_grid_to_up(self, grid):
        """
        Wir iterieren durch die Matrix und holen jede Spalte aus der Matrix.
        Die Spalte wird zum Zeilenvektor umgewandelt und in die update_row_to_left Methode übergeben.
        """
        updated_grid = []
        for i in range(len(grid)):
            row_vector = self.row_vector_from_matrix(grid, i)

            updated_grid.append(self.update_row_to_left(row_vector))

        return self.transpose_grid(updated_grid)

    @staticmethod
    def add_random_tile(grid, amount=1):
        """
        Sucht die Spielfeldmatrix nach Feldern mit einer 0 ab und weist einem davon zufällig den Wert 2 oder 4 zu.
        """
        empty_fields = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    empty_fields.append((i, j))

        if len(empty_fields) > 0:
            for i in range(amount):
                random_field = choice(empty_fields)
                random_value = choice([2, 4])
                grid[random_field[0]][random_field[1]] = random_value

    def get_grid_value(self, i, j):
        return self.grid[i][j]

    @staticmethod
    def is_grid_full(grid):
        has_empty_fields = False

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    has_empty_fields = True
                    break

        return not has_empty_fields

    @staticmethod
    def grid_has_equal_adjacent_fields(grid):
        """
        Test, ob es benachbarte Felder mit gleichem Wert gibt
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    # fixme: there should be a better solution to ensure that the index will not be out of range
                    try:
                        if grid[i][j] == grid[i][j + 1] or grid[i][j] == grid[i + 1][j]:
                            return True
                    except IndexError:
                        """ Es müssen keine Informationen protokolliert werden, da wir den Grund kennen"""
                        pass
        return False

    def should_update(self):
        """
        Test, ob ein weiterer Zug möglich ist
        """

        if self.grid_has_empty_field():
            return True
        elif self.grid_has_equal_adjacent_fields(self.grid):
            return True

        return False

    def grid_has_empty_field(self):
        """
        Test, ob es ein Feld mit 0 gibt
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    return True
        else:
            return False
