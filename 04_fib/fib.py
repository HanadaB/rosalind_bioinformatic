"""Fibonacci sequence """
from functools import lru_cache

@lru_cache(maxsize=None)
def rabbits(n: int , k: int) -> int:
    if n == 1 or n == 2  :
        return 1

    return rabbits(n-1, k) + k * rabbits(n-2 , k)


def main():
    n, k = map(int, input().split())
    print(f"The population of rabbits after {n} month is: {rabbits(n, k)}")


if __name__ == "__main__":
    main()