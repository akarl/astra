from prompt import prompt


def choice(items):
    choices = {
        unicode(i + 1): item
        for i, item in enumerate(items)
    }
    choosen = None

    for k, v in choices.items():
        print '(%s) %s' % (k, v)

    while choosen not in choices.keys():
        choosen = prompt(u'Choose: ')

    return choices[choosen]
