import string
import random

def randomString(size=32, chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
