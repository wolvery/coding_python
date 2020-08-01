from collections import defaultdict
from typing import Dict, List, Tuple

ORIGINAL_NAME = 0
SORTED_NAME = 1
EMPTY = ""


class Finder:

    def __init__(self, string_list: List[str]) -> None:
        """
        Finder search words which matches the same quantity of characters to a given word.
        :param string_list: List of words to be searched on
        :rtype: Finder
        """
        self.conjunct = self.adjusts(string_list)

    @staticmethod
    def adjusts(string_list: List[str]) -> Dict[int, List[Tuple[str, str]]]:
        """
        Adjust a given string lists to a schema of dict[Length: sublist of words].
        :param string_list: List of words to be adjusted
        :rtype: dict[Length: sublist of words]
        """
        conjunct = defaultdict(list)

        for element in string_list:
            conjunct[len(element)] += [(element, EMPTY.join(sorted(element)))]

        return conjunct

    def find(self, word: str) -> List[str]:
        """
        Generates a list of matched words to an input word.
        :param word: Parameter to be searched on.
        :rtype: List of matched words registered to this instance of Finder.
        """
        matched_words: List[str] = list()
        length = len(word)
        sorted_word = EMPTY.join(sorted(word))

        for element in self.conjunct[length]:
            if sorted_word == element[SORTED_NAME]:
                matched_words += [element[ORIGINAL_NAME]]

        return matched_words




