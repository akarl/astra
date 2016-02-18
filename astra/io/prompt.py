from pygments.token import Token
from prompt_toolkit.shortcuts import prompt as pt_prompt

from astra import events


class Prompt(events.Listener):
    cli = None
    current_time = None

    def __call__(self, message):
        cmd = pt_prompt(
            message,
            get_bottom_toolbar_tokens=self.get_bottom_toolbar_tokens,
            patch_stdout=True
        )
        return cmd.split()

        events.fire('cmd:%s' % cmd[0], cmd)

    def get_bottom_toolbar_tokens(self, cli):
        self.cli = cli

        if self.current_time is None:
            return []

        return [
            (Token.Toolbar, self.current_time.isoformat()),
            # (Token.Toolbar, u' | '),
            # (Token.Toolbar, u'Paused' if self.paused else self.speed),
            # (Token.Toolbar, u' | '),
            # (Token.Toolbar, unicode(GAME.current_system))
        ]

    @events.on('game_tick')
    def redraw(self, event, date, prev_date):
        self.current_time = date

        if self.cli:
            self.cli.request_redraw()

prompt = Prompt()
