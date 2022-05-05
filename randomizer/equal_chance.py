import sys
import random


def ra(amount):
    a = 0
    for _ in range(amount):
        a += random.randint(0, 1)
    return a - amount // 2


if __name__ == "__main__":
    amount = sys.argv[1]
    print(ra(int(amount)))

