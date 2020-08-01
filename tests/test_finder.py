import pytest
from finder import Finder
from typing import List


@pytest.mark.parametrize("string_list, input, expected", [
    (['asd', 'asdd', 'fre', 'glk', 'lkm'], 'sad', ['asd']),
    (['complicated', 'happy', 'ppyha', 'sas', 'zzzz'], 'happy', ['happy', 'ppyha']),
    (['oom', 'oom', 'moo', 'omo'], 'omo', ['oom', 'oom', 'moo', 'omo']),
    (['sadapop', 'sada', 'pop', 'sasasasa', 'sasasasa'], 'zzz', []),
])
def test_finder(string_list: List<str>, input: str, expected: List<str>):
    instance = Finder(string_list)
    result = instance.find(input)
    # I can not guarantee if there is repeated
    assert  sorted(result) == sorted(expected)