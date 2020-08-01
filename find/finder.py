from collections import defaultdict
from typing import Dict, List, Tuple

ORIGINAL_NAME = 0
SORTED_NAME = 1


class Finder:

    def __init__(self, string_list: List[str]):
        self.conjunct = self.adjusts(string_list)

    @staticmethod
    def adjusts(string_list: List[str]) -> Dict[int, List[Tuple[str, str]]]:
        conjunct = defaultdict(list)

        for element in string_list:
            conjunct[len(element)] += [(element, sorted(element))]

        return conjunct

    def find(self, word: str) -> List[str]:
        matched_words: List[str] = list()
        length = len(word)
        sorted_word = sorted(word)

        for element in self.conjunct[length]:
            if sorted_word == element[SORTED_NAME]:
                matched_words += element[ORIGINAL_NAME]

        return matched_words




