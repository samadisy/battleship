from fastapi import FastAPI
from enum import Enum


class ShipType(Enum):
    CARRIER = "Carrier"
    BATTLESHIP = "Battleship"
    CRUISER = "Cruiser"
    SUBMARINE = "Submarine"
    DESTROYER = "Destroyer"

class HitMiss(Enum):
    MISS = 0
    HIT = 1
app = FastAPI()

@app.get("/start_game")
def start_game():
    return {
        "game_phase": "SETUP",
        "board_state": [['-' for _ in range(10)] for _ in range(10)],
        "ships": [(ShipType.CARRIER, 5, [[-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS]]),
                  (ShipType.BATTLESHIP, 4, [[-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS]]),
                  (ShipType.CRUISER, 3, [[-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS]]),
                  (ShipType.SUBMARINE, 3, [[-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS]]),
                  (ShipType.DESTROYER, 2, [[-1, -1, HitMiss.MISS], [-1, -1, HitMiss.MISS]])]
    }