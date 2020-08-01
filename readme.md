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
* I do not need to check words with length bigger or smaller than the input.
* The word inside of string_list must match with the quantity of characters. 
I can reach this with an order at both of them and comparing them afterwards.
* 