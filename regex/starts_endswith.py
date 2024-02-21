"""
Learning how to validate the star and end of string with regex
^: starts with
$: ends with

[^A-Z]: Anything but A-Z characters

"""

import re

cpf = 'a 123.456.789-00'

#should start with nnn.
print(re.findall(r'^((?:[0-9]{3}.){2}[0-9]{3}-[0-9]{2})', cpf))

#should end with -nn
print(re.findall(r'((?:[0-9]{3}.){2}[0-9]{3}-[0-9]{2})$', cpf))
