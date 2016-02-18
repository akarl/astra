import datetime
import random

from astra.io.output import output
from astra.actors.system import System


class GameWorld(object):
    viewed_system = None

    def __init__(self, data=None):
        self.data = data or {}

    @classmethod
    def load(cls, save_file):
        with open(filepath, 'r') as f:
            data = pickle.load(f)

        return cls(data=data)

    @classmethod
    def new(cls, name):
        data = {}

        system = System(name)

        tries = 0
        while len(system.habitable_bodies) < 3:
            system.generate()
            tries += 1

        body = random.choice(system.habitable_bodies)
        body.create_colony()
        body.habitants = random.randint(1000, 3000) * 1000000

        data['systems'] = {
            system.name.lower(): system
        }
        data['current_system'] = system
        data['date'] = datetime.datetime(2377, 1, 1)
        data['start_date'] = datetime.datetime(2377, 1, 1)

        output('Generated starting system (%s tries).' % tries)

        return cls(data=data)

    @property
    def systems(self):
        return self.data['systems']

    @property
    def date(self):
        return self.data['date']

    @date.setter
    def date(self, val):
        self.data['date'] = val
