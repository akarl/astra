from astra import events
import pytest


class TestEvents(object):
    def test_abc(self):
        class GameObject(events.Listener):

            @events.on('time_elapsed')
            def do_something(self, event, arg):
                raise Exception('%s %s' % (event, arg))
                pass

        g = GameObject()

        with pytest.raises(Exception) as exc_info:
            events.fire('time_elapsed', 'woho')

        assert str(exc_info.value) == 'time_elapsed woho'
