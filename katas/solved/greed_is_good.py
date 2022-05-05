# Solved!

from collections import Counter


def score(dice):
    res = 0
    counter = Counter(dice)
    rewards = {1: (1000, 100), 2: (200, 0), 3: (300, 0), 4: (400, 0), 5: (500, 50), 6: (600, 0)}
    for k, v in counter.items():
        big_reward = rewards[k][0]
        small_reward = rewards[k][1]
        if small_reward:
            if v == 3:
                res += big_reward
            elif v > 3:
                res += big_reward + small_reward * (v - 3)
            else:
                res += small_reward * v
        else:
            if v >= 3:
                res += big_reward
    return res


if __name__ == "__main__":
    assert score([5, 1, 3, 4, 1]) == 250
    assert score([1, 1, 1, 3, 1]) == 1100
    assert score([2, 4, 4, 5, 4]) == 450
