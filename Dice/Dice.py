import random

def throw():
    results = []
    for i in range(2):
        num = random.randint(1,6)
        results.append(num)

    return results
