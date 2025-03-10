import os
import random

import a_lib

# OK
random.SystemRandom()

# Errors
random.Random()
random.random()
random.randrange()
random.randint()
random.choice()
random.choices()
random.uniform()
random.triangular()
random.randbytes()

# Unrelated
os.urandom()
a_lib.random()


# https://github.com/astral-sh/ruff/issues/15522
map(random.randrange, [])
foo = random.randrange
