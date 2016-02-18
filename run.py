from astra.game.loop import GameLoop
from astra.menus.main_menu import MainMenu
from astra.menus.save_load import SaveLoadMenu

if __name__ == '__main__':

    game_world = SaveLoadMenu.display()

    game_loop = GameLoop(game_world)
    game_loop.start()

    MainMenu.display()
