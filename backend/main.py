from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tennis Tracker!"}

players = []

def get_next_id():
    next_id = len(players) + 1
    return next_id

class PlayerCreate(BaseModel):
    name: str
    age: int
    country: Optional[str] = None

class Player(BaseModel):
    id: int
    name: str
    age: int
    country: Optional[str] = None

@app.post("/players")
def create_player(player: PlayerCreate):
    player_id = get_next_id()
    new_player = Player(id = player_id, name = player.name, age = player.age, country = player.country)
    players.append(new_player)
    return new_player

@app.get("/players")
def get_players():
    return players