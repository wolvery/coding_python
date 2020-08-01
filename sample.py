from timeit import timeit
from typing import List
from find.finder import Finder


def measure() -> None:
    string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
    word = 'sad'
    print("hello")
    print(f"50K runs: {timeit(lambda: sample(string_list, word), number=50000)}")
    print(f"Large initialization: {timeit(lambda: sample(string_list * 100, word))}")

    print(f"Edge case (big words impact sorting): {timeit(lambda: sample([word*10000] * 1000, word))}")


def sample(string_list: List[str], word: str) -> None:

    finder = Finder(string_list)

    finder.find(word)


if __name__ == '__main__':
    measure()
