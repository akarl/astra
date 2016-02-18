from threading import Thread, Event
from datetime import timedelta, datetime

from astra import events
from astra.menus.base_menu import OptionsMenu
from astra.io.output import output
from time import sleep


class GameLoop(events.Listener):
    running = Event()
    speed = 1

    def __init__(self, game_world):
        super(GameLoop, self).__init__()
        self.game_world = game_world

    def start(self):
        self.thread = Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        while True:
            self.running.wait()

            prev_date = self.game_world.date
            self.game_world.date = prev_date + timedelta(days=1)

            before = datetime.now()
            events.fire(
                'game_tick',
                self.game_world.date,
                prev_date
            )
            after = datetime.now()

            delta = (after - before).total_seconds()
            delta = 1.0 - delta
            sleep_time = delta / self.speed

            if sleep_time > 0:
                sleep(sleep_time)

    @events.on('cmd:play')
    def play(self, event, cmd):
        if len(cmd) == 2:
            self.speed = int(cmd[1])
        self.running.set()

    @events.on('cmd:stop')
    def stop(self, event, cmd):
        self.running.clear()

    @events.on('cmd:view')
    def view(self, event, cmd):
        if not self.game_world.viewed_system:
            system = OptionsMenu.display(self.game_world.systems.values())
            self.game_world.viewed_system = system

        for body in self.game_world.viewed_system.bodies:
            output(body)
