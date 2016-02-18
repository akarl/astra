from astra.menus.base_menu import BaseMenu
from astra import events


class MainMenu(BaseMenu):
    def handle_cmd(self, cmd):
        events.fire('cmd:%s' % cmd[0], cmd)
