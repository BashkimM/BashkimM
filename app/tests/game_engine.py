import pytest

from app.game_engine import GameEngine


class TestGameEngine:
    """
    Following the concept of test driven development, this class is used to test the GameEngine during development.
    Further, it gives the ability to refactor or enhance the GameEngine without the need to "play" the game and hoping
    certain circumstances to occur.
    Set up by Marcel Tams and worked on together with Eike Gosch.
    """

    """
    Test cases for the column to left. List of tuples with the following structure:
    (expected_list: list, input_data: list)
    """
    columns_test_data_to_left = [
        ([4, 0, 0, 0], [0, 0, 2, 2]),
        ([4, 0, 0, 0], [0, 2, 0, 2]),
        ([4, 2, 0, 0], [0, 2, 2, 2]),
        ([4, 2, 0, 0], [2, 0, 2, 2]),
        ([4, 4, 4, 0], [4, 2, 2, 4]),
    ]

    """
    Test cases for the column to right. List of tuples with the following structure:
    (expected_list: list, input_data: list)
    """
    columns_test_data_to_right = [
        ([0, 0, 0, 4], [0, 0, 2, 2]),
        ([0, 0, 0, 4], [0, 2, 0, 2]),
        ([0, 0, 2, 4], [0, 2, 2, 2]),
        ([0, 0, 2, 4], [2, 0, 2, 2]),
        ([0, 4, 4, 4], [4, 2, 2, 4])
    ]

    """
    Test cases for grid to left. List of tuples with the following structure:
    (expected_list: list, input_data: list)
    """
    test_data_grid_to_left = [
        ([
             [4, 2, 0, 0],
             [4, 4, 0, 0],
             [8, 4, 2, 0],
             [8, 4, 0, 0]
         ],
         [
             [2, 2, 2, 0],
             [2, 2, 2, 2],
             [0, 8, 4, 2],
             [4, 4, 2, 2]
         ]),
    ]

    """
    Test cases for grid to right. List of tuples with the following structure:
    (expected_list: list, input_data: list)
    """
    test_data_grid_to_right = [
        ([
             [0, 0, 0, 4],
             [0, 0, 2, 4],
             [0, 0, 2, 4],
             [0, 4, 4, 4],
         ],
         [
             [0, 2, 0, 2],
             [0, 2, 2, 2],
             [2, 0, 2, 2],
             [4, 2, 2, 4]
         ]),
    ]

    """
        Test cases for grid to up. List of tuples with the following structure:
        (expected_list: list, input_data: list)
        """
    test_data_grid_to_up = [
        ([
             [2, 2, 2, 0],
             [2, 2, 2, 2],
             [0, 8, 4, 2],
             [4, 4, 2, 2]
         ],
         [
             [4, 4, 4, 4],
             [4, 8, 4, 2],
             [0, 4, 2, 0],
             [0, 0, 0, 0]
         ]),
    ]

    """
        Test cases for grid to down. List of tuples with the following structure:
        (expected_list: list, input_data: list)
        """
    test_data_grid_to_down = [
        ([
             [2, 2, 2, 0],
             [2, 2, 2, 2],
             [0, 8, 4, 2],
             [4, 4, 2, 2]
         ],
         [
             [0, 0, 0, 0],
             [0, 4, 4, 0],
             [4, 8, 4, 2],
             [4, 4, 2, 4]
         ]),
    ]

    """
        Test case for multiple iterations on the update_grid_to_down method List of tuples with the following structure:
        (expected_list: list, input_data: list)
        """
    test_data_grid_to_down_multiple = [
        ([
             [2, 2, 0, 0],
             [2, 2, 2, 2],
             [0, 8, 4, 2],
             [0, 4, 2, 2]
         ],
         [
             [0, 0, 0, 0],
             [0, 4, 2, 0],
             [0, 8, 4, 2],
             [4, 4, 2, 4]
         ]),
    ]

    test_data_transpose_grid = [
        ([
             [4, 0, 2, 2],
             [4, 8, 2, 2],
             [2, 4, 2, 2],
             [2, 2, 2, 0]
         ],
         [
             [4, 4, 2, 2],
             [0, 8, 4, 2],
             [2, 2, 2, 2],
             [2, 2, 2, 0]
         ]),
        ([
             [4, 4, 0, 0],
             [4, 8, 4, 0],
             [4, 4, 2, 0],
             [2, 4, 0, 0]],
         [
             [4, 4, 4, 2],
             [4, 8, 4, 4],
             [0, 4, 2, 0],
             [0, 0, 0, 0]
         ])
    ]

    test_data_is_grid_full = [
        ([
             [4, 4, 4, 4],
             [4, 8, 4, 2],
             [4, 8, 4, 2],
             [4, 8, 4, 2]
         ], True),
        ([
             [4, 4, 4, 4],
             [4, 8, 4, 2],
             [4, 8, 4, 2],
             [0, 8, 4, 2]
         ], False),
    ]

    def test_setup_grid(self):
        expected_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        result = GameEngine.setup_grid(4)

        assert expected_grid == result

    def test_setup_grid_with_size_of_5(self):
        expected_grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        result = GameEngine.setup_grid(5)

        assert expected_grid == result

    @pytest.mark.parametrize("expected,test_input", columns_test_data_to_left)
    def test_update_row_to_left(self, expected, test_input):
        game = GameEngine()

        assert game.update_row_to_left(test_input) == expected

    @pytest.mark.parametrize("expected,test_input", columns_test_data_to_right)
    def test_update_row_to_right(self, test_input, expected):
        game = GameEngine()
        assert game.update_row_to_right(test_input) == expected

    @pytest.mark.parametrize("expected,test_input,vector_column", [
        ([4, 2, 2, 8], [
            [4, 0, 0, 0],
            [2, 0, 2, 2],
            [2, 0, 2, 2],
            [8, 0, 2, 2]],
         0),
        ([16, 2, 2, 8], [
            [2, 4, 8, 16],
            [4, 8, 16, 2],
            [2, 0, 32, 2],
            [2, 0, 0, 8]],
         3),
    ])
    def test_vector_column_from_matrix(self, test_input, expected, vector_column):
        game = GameEngine()
        assert game.row_vector_from_matrix(test_input, vector_column) == expected

    @pytest.mark.parametrize("expected,test_input", test_data_grid_to_left)
    def test_update_grid_to_left(self, test_input, expected):
        game = GameEngine()
        assert game.update_grid_to_left(test_input) == expected

    @pytest.mark.parametrize("expected,test_input", test_data_grid_to_right)
    def test_update_grid_to_right(self, test_input, expected):
        game = GameEngine()
        assert game.update_grid_to_right(test_input) == expected

    @pytest.mark.parametrize("test_input,expected,", test_data_grid_to_up)
    def test_update_grid_to_up(self, test_input, expected):
        game = GameEngine()

        assert game.update_grid_to_up(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", test_data_grid_to_down)
    def test_update_grid_to_down(self, test_input, expected):
        game = GameEngine()
        assert game.update_grid_to_down(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", test_data_grid_to_down_multiple)
    def test_update_grid_to_down_twice(self, test_input, expected):
        game = GameEngine()

        first_iteration = game.update_grid_to_down(test_input)
        second_iteration = game.update_grid_to_down(first_iteration)
        third_iteration = game.update_grid_to_down(second_iteration)
        assert third_iteration == expected

    @pytest.mark.parametrize("test_input,expected", test_data_transpose_grid)
    def test_transpose_grid(self, test_input, expected):
        game = GameEngine()

        assert game.transpose_grid(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", test_data_is_grid_full)
    def test_is_grid_full(self, test_input, expected):
        game = GameEngine()

        assert game.is_grid_full(test_input) == expected

    test_data_is_grid_full_with_zero = [
        ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], False),
        ([[2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], True),
        ([[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], True),
        ([[2, 4, 8, 16], [16, 8, 4, 2], [32, 64, 128, 16], [4, 2, 16, 32]], False),
    ]

    @pytest.mark.parametrize("test_input,expected", test_data_is_grid_full_with_zero)
    def test_has_equal_adjacent_fields(self, test_input, expected):
        game = GameEngine()

        assert game.grid_has_equal_adjacent_fields(test_input) == expected
