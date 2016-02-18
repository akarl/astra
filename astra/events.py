from collections import defaultdict
from threading import RLock


EVENTS = [
    'time_elapsed',
    'game_tick',
    'cmd:play',
    'cmd:stop',
    'cmd:view'
]

handlers = defaultdict(set)
event_lock = RLock()


def on(events):
    if not hasattr(events, '__iter__'):
        events = [events]

    for event in events:
        assert event in EVENTS

    def decorate(func):
        func.events = events
        return func

    return decorate


def fire(event, *args, **kwargs):
    # with event_lock:
    for func in handlers[event]:
        func(event, *args, **kwargs)


class Listener(object):
    def __init__(self, *args, **kwargs):
        for f in dir(self):
            try:
                f = getattr(self, f)
            except Exception:
                continue

            if hasattr(f, 'events'):
                for event in f.events:
                    handlers[event].add(f)

__all__ = [Listener, fire, on]
