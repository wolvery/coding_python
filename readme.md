# Introduction
## Relayr Onboarding Python Test

` You will design & write a Python class that accepts a list of strings in the constructor. The
class will expose a find function that accepts a string. The function will return all strings from
the list that contain the exact same characters as the string passed into it. The order of the
characters in the strings is not relevant.

 
 An example:

 
string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm'];


finder = Finder(string_list);


finder.find('sad')


returns ['asd']
`

From the example, I should return elements with the same quantity of characters from input.


Some assumptions: 
* The word inside of string_list must match with the quantity of each characters from input. 
I can reach this with an order at both of them and comparing them afterwards. 
* If multiple find will be executed, it would be interesting to reduce the ordering from the list to happen again. 
A possible solution would perform sort at each element of string_list just once and store it.




Test Framework used:
pytest
Reasons:
* Familiarity with it.
* Capacity to execute unittest as well.
* Appreciates the fixture and parametrize functionality.


## HOW TO
# test
pytest tests
pylint  find
mypy find
# execute
`docker build . -t test`
`docker run test`
OR 
`docker run -ti test bash`

