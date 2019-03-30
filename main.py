from game import Game
from player import Player
from console import Console

if __name__ == '__main__':
    player = Player()
    console = Console()
    game = Game(player, console)
    game.play()