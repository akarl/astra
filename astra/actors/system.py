from operator import attrgetter
from uuid import uuid4
import random
import math

from astra import events
from astra.io.output import output
from astra.actors.base import Actor


class System(Actor):
    name = u''
    jump_points = []
    bodies = []
    construction_queue = []
    installations = {
        'factories': 0,
        'mines': 0,
    }

    def __init__(self, name):
        self.name = name
        super(Actor, self).__init__()

    def generate(self):
        self.bodies = []

        for i in range(random.randint(0, 15)):
            self.bodies.append(Body(
                system=self,
                distance=random.uniform(0.1, 70)
            ))

        self.bodies = sorted(self.bodies, key=attrgetter('distance'))

    @property
    def habitable_bodies(self):
        return [b for b in self.bodies if b.is_habitable]

    def get_body(self, item_from_sun):
        return self.bodies[item_from_sun - 1]

    def __unicode__(self):
        return self.name


class Body(Actor):
    _name = None
    is_habitable = False
    colony = False
    habitants = 0

    distance = 0

    position = (0.0, 0.0)

    # Orbital speed in radians / day
    orbital_speed = 0

    _age = 1

    def __init__(self, system, distance):
        self.distance = distance
        self.system = system

        if 0.7 <= self.distance <= 1.6:
            self.is_habitable = True  # random.choice([True, True, True, False])

        self.orbital_speed = (math.pi * 2) / (365.25 * self.distance)
        self.position = (0.0, self.distance)

        self._age = random.randint(1, 5000)

        super(Body, self).__init__()

    @events.on('game_tick')
    def update_position(self, event, new_date, prev_date):
        delta = new_date - prev_date

        self._age += delta.days

        self.position = (
            self.distance * math.cos(self.orbital_speed * self._age),
            self.distance * math.sin(self.orbital_speed * self._age)
        )

    @property
    def name(self):
        if self._name:
            return self._name
        else:
            return u'%s %s' % (
                self.system.name,
                self.system.bodies.index(self) + 1
            )

    def create_colony(self):
        self.colony = True

    def __unicode__(self):
        suffixes = []

        if self.colony:
            suffixes.append(str(self.habitants / 1000000) + u'M')
        elif self.is_habitable:
            suffixes.append(u'H')

        if suffixes:
            return u'%s (%s)' % (self.name, u''.join(suffixes))

        return self.name

    def view(self):
        print u'Name: ', self.name
        print u'Colony: ', self.colony
        print u'Habitable: ', self.is_habitable
        print u'Distance from sun (AU): ', self.distance
