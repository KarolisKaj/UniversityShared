import random

attribute_actions = dict([('dr', lambda rate: random.random() < rate), ('to', 4127), ('jack', 4098)])
