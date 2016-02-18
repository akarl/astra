from os import walk
from os.path import expanduser, join

from astra.io.output import output
from astra.menus.game_creator import GameCreatorMenu
from astra.menus.base_menu import OptionsMenu
# from astra.game.game_world import GameWorld


class SaveLoadMenu(OptionsMenu):
    options = ['new']
    prompt_text = u'New/Load Game: '
    save_dir = join(expanduser('~'), '.astra/')

    def get_options(self):
        try:
            save_files = next(walk(self.save_dir))[2]
        except StopIteration:
            return self.options
        else:
            return self.options + save_files

    def handle_choice(self, choice):
        if choice == 'new':
            return GameCreatorMenu.display()

        # return GameWorld(data=save_file)
        output(choice)
