import pytest
from find.finder import Finder
from typing import Dict, List, Tuple


@pytest.mark.parametrize("string_list, expected", [
    (['asd', 'das'], {3: [('asd', 'ads'), ('das', 'ads')]}),
    (['asd', 'das', 'asdd'], {3: [('asd', 'ads'), ('das', 'ads')], 4: [('asdd', 'adds')]})

])
def test_init_finder(string_list: List[str], expected: Dict[int, List[Tuple[str, str]]]):
    """
    Test that init works properly to adjust string_list.
    """
    instance = Finder(string_list)
    assert all(instance.conjunct[length] == expected[length] for length in expected.keys())


@pytest.mark.parametrize("string_list, word, expected", [
    (['asd', 'asdd', 'fre', 'glk', 'lkm'], 'sad', ['asd']),
    (['complicated', 'happy', 'ppyha', 'sas', 'zzzz'], 'happy', ['happy', 'ppyha']),
    (['oom', 'oom', 'moo', 'omo'], 'omo', ['oom', 'oom', 'moo', 'omo']),
    (['sadapop', 'sada', 'pop', 'sasasasa', 'sasasasa'], 'zzz', []),
])
def test_finder(string_list: List[str], word: str, expected: List[str]):
    """
    Test that finder.find collects the correct elements.
    """

    instance = Finder(string_list)
    result = instance.find(word)
    # I can not guarantee if there is repeated
    assert sorted(result) == sorted(expected)