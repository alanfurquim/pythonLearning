"""
Learning about the search, findall, sub and compile functions from regex library
"""
import re

string = 'This is a test of regular expressions'

#search the first ocurrence of the regular expression in string
print(re.search(r'test', string))

#search all ocurrences of the regular expression in string
print(re.findall(r'test', string))

#replace the regex match to the defined substring in string
print(re.sub(r'test', '@alanfurquim', string))

#compile the regular expression. used when the regex is necessary more than 1 time
regexp = re.compile(r'test')

print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('@alanfurquim', string))
