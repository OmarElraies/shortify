import string
import random


def url_shortener():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

