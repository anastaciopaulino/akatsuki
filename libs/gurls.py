import string
import random

def gurls():
    characters = string.ascii_letters + string.digits

    password = "".join(random.choice(characters) for x in range(random.randint(50, 100)))

    return password