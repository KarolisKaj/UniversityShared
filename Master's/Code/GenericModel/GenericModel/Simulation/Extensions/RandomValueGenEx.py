import random

def generate_gauss_timeout(env, mid_point):
    generated_timeout = random.gauss(mid_point, int((mid_point * 0.1)))
    return env.timeout(generated_timeout);
