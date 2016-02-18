from astra.menus.base_menu import BooleanMenu, BaseMenu
from astra.game_world import GameWorld


class GameCreatorMenu(BooleanMenu):
    prompt_text = u'Are you satisfied?'
    data = {}

    def before_prompt(self):
        name = BaseMenu.display(u'Starting system name?')
        self.data['name'] = name[0]

    def handle_boolean(self, yes):
        if yes:
            return GameWorld.new(**self.data)
