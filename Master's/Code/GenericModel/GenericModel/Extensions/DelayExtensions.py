import random

def latency(env, latency):
    return self.env.timeout(latency)

def rand_latency(env, min, max):
    latency = random.randint(min, max)
    return latency(env,latency)
