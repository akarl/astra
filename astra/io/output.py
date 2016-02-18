from __future__ import print_function
from threading import RLock

output_lock = RLock()


def output(text):
    with output_lock:
        print(unicode(text))
