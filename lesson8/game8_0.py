# console game

# | | | | |    | | | | |   | | | | |
# | | | | |    | | | | |   | | | | |
# | | | | |    | | | | |   | | |x| |
# | | | |x|    | | |x| |   | | | | |

from datetime import datetime
import json
from random import randint


size_n = 10
size_m = 10


def log(action):

    current_time = datetime.strftime(datetime.now(), "%H:%M:%S")
    message = f"[{current_time}] {action}"

    print(message)
    with open("logs.txt", "a") as file:
        file.write(f"{message}\n")


def generate_map(n, m):

    log(f"Generating map...")

    game_map = []

    for _ in range(n):
        row = [" " for _ in range(m)]
        game_map.append(row)

    log(f"Map has been generated")
    
    return game_map


def print_map(game_map):

    for row in game_map:
        print(f"|"+"|".join(row)+f"|")


def generate_world(game_map):

    log(f"Generating world...")

    objs = {"X": 1, "O": 3, "&": 3, "_": 3}
    size_n, size_m = len(game_map), len(game_map[0])
    rnd_cells = []

    for obj, n in objs.items():
        for i in range(n):
            rnd_cell = randint(0, size_n - 1), randint(0, size_m - 1)
            if rnd_cell not in rnd_cells:
                rnd_cells.append(rnd_cell)
            else:
                rnd_cell = randint(0, size_n - 1), randint(0, size_m - 1)
                rnd_cells.append(rnd_cell)

            if obj == "X":
                char_position = rnd_cell

            game_map[rnd_cell[0]][rnd_cell[1]] = obj

    log(f"World has been generated")

    return game_map, list(char_position)


def move(direction, game_world, char_position):

    log(f"Moving {direction} from position {char_position}")

    game_world[char_position[0]] [char_position[1]] = " "

    if direction == "down":
        char_position[0] += 1
    elif direction == "up":
        char_position[0] -= 1
    elif direction == "left":
        char_position[1] -= 1
    elif direction == "right":
        char_position[1] += 1

    game_world[char_position[0]] [char_position[1]] = "X"

    log(f"New position {char_position}")

    return game_world, char_position # char_position - не було


def save_game(game_world, char_position):

    log("Saving game...")

    game_save = {"game_world": game_world, "char_position": char_position}
    
    with open("save.txt", "w") as file:
        json.dump(game_save, file)

    log("Game has been saved")


def load_game():

    log(f"Loading game...")

    with open("save.txt") as file:
        game_save = json.load(file)
    
    game_world = game_save["game_world"]
    char_position = game_save["char_position"]

    log("Game has been loaded")

    return game_world, char_position


game_map = generate_map(size_n, size_m)
game_world, char = generate_world(game_map)
print_map(game_world)

while True:

    action = input("Choose action: ")

    if action not in ("move", "save", "load"):
        log (f"Wrong action. Try again")
        continue

    if action == "save":
        save_game(game_world, char)
        continue
    elif action == "load":
        game_world, char = load_game()
        print_map(game_world)
        print(char)
        continue

    direction = input("Choose direction: ")

    if direction not in ("up", "down", "left", "right"):
        log (f"Wrong direction. Try again")
        continue

    game_world, char = move(direction, game_world, char)
    print_map(game_world)
