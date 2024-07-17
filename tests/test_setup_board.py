import pytest
import requests

class TestSetupBoard:
    @pytest.fixture
    def response(self):
        return requests.get("http://127.0.0.1:5000/start_game")

    def test_start_game_exists(self, response):
        assert response.status_code == 200

    def test_start_game_in_setup_phase(self, response):
        assert response.json()['game_phase'] == "SETUP"

    def test_start_game_returns_empty_board(self, response):
        expected_board_state = [['-' for _ in range(10)] for _ in range(10)]
        assert response.json()['board_state'] == expected_board_state

    def test_start_game_returns_available_ships(self, response):
        expected_ships = [
            ['Carrier', 5, [[-1, -1, 0], [-1, -1, 0], [-1, -1, 0], [-1, -1, 0], [-1, -1, 0]]],
            ['Battleship', 4, [[-1, -1, 0], [-1, -1, 0], [-1, -1, 0], [-1, -1, 0]]],
            ['Cruiser', 3, [[-1, -1, 0], [-1, -1, 0], [-1, -1, 0]]],
            ['Submarine', 3, [[-1, -1, 0], [-1, -1, 0], [-1, -1, 0]]],
            ['Destroyer', 2, [[-1, -1, 0], [-1, -1, 0]]]
        ]
        assert response.json()['ships'] == expected_ships



