from astra.io.prompt import prompt
from astra.io.output import output


class BaseMenu(object):
    prompt_text = u'Your command Sir'
    promt_suffix = u': '

    def __init__(self, prompt_text=None):
        if prompt_text:
            self.prompt_text = prompt_text

    @classmethod
    def display(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)
        return instance.run()

    def prompt(self):
        return prompt(self.prompt_text + self.promt_suffix)

    def before_prompt(self):
        pass

    def run(self):
        while True:
            self.before_prompt()
            cmd = self.prompt()

            if not cmd:
                continue

            if cmd[0] == 'exit':
                return

            result = self.handle_cmd(cmd)

            if result is not None:
                return result

    def handle_cmd(self, cmd):
        return cmd


class BooleanMenu(BaseMenu):
    prompt_text = u'Yes or No?'
    promt_suffix = u' [y/n]: '

    def handle_boolean(self, yes):
        return yes

    def handle_cmd(self, cmd):
        cmd = cmd[0]

        if cmd in ['y', 'yes']:
            return self.handle_boolean(True)
        if cmd in ['n', 'no']:
            return self.handle_boolean(False)

        output('Please choose yes or no.')


class OptionsMenu(BaseMenu):
    prompt_text = u'Please choose'
    options = None

    def __init__(self, options=None):
        self.options = options or self.options or []

    def get_options(self):
        return self.options

    def before_prompt(self):
        self.choices = {}
        for i, option in enumerate(self.get_options()):
            i = unicode(i)
            name = unicode(option).lower()

            self.choices[name] = option
            self.choices[i] = option

            output(u'(%s) %s' % (i, name))

    def handle_cmd(self, cmd):
        index = cmd[0]
        if index in self.choices:
            return self.handle_choice(self.choices[index])

    def handle_choice(self, choice):
        return choice
