from collections import defaultdict
from typing import Dict, List

EMPTY = ""


class Finder:

    def __init__(self, string_list: List[str]) -> None:
        """
        Finder search words which matches the same quantity of characters to a given word.
        :param string_list: List of words to be searched on
        :rtype: Finder
        """
        self.conjunct: Dict[str, List[str]] = self.adjusts(string_list)

    @staticmethod
    def adjusts(string_list: List[str]) -> Dict[str, List[str]]:
        """
        Adjust a given string lists to a schema of dict[sorted_word: sublist of string_list].
        :param string_list: List of words to be adjusted
        :rtype: dict[sorted_word: sublist of string_list]
        """
        conjunct: Dict[str, List[str]] = defaultdict(list)

        for element in string_list:
            sorted_element = EMPTY.join(sorted(element))
            conjunct[sorted_element].append(element)

        return conjunct

    def find(self, word: str) -> List[str]:
        """
        Generates a list of matched words to an input word.
        :param word: Parameter to be searched on.
        :rtype: List of matched words registered to this instance of Finder.
        """
        matched_words: List[str] = list()
        sorted_word = EMPTY.join(sorted(word))

        if sorted_word in self.conjunct:
            return self.conjunct[sorted_word]

        return matched_words
