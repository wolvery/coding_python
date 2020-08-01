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
* It appears that the list may contains any words bigger or smaller than the input.
I do not need to check words which length differs from the input. 
If this occurs frequently, I could use a dictionary of lengths as key
and group the words with the same length. 
* The word inside of string_list must match with the quantity of each characters from input. 
I can reach this with an order at both of them and comparing them afterwards. 
* If multiple find will be executed, it would be interesting to reduce the ordering from the list to happen again. 
A possible solution would perform sort at each element of string_list just once and store it as tuple.
This will increase the space complexity to 2n. N being the length of string_list.


Test Framework used:
pytest
Reasons:
* Familiarity with it.
* Capacity to execute unittest as well.
* Appreciates the fixture and parametrize functionality.
