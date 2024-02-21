"""
Learning more about groups in regex.

[abc]: any
(abc): this sequence

(): creates group 
\n: references group
    (): \1
    () (): \1 \2
    (())(): \1 \2 \3

(?:): creates group but does not save
(?P<name>): creates a named group
"""
import re

text = """
<p>tag 1</p> <p>tag 2</p> <p>tag 3</p> <div>tag 4</div>
"""

tags = re.findall(r'<([pdiv]{1,3})>(.*?)<\/\1>', text)

#entering all groups
for tag in tags:
    print(tag[1])

#replacing regex
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', text))

#validating cpf format
cpf = '123.456.789-00'
print(re.findall(r'((?:[0-9]{3}.){2}[0-9]{3}-[0-9]{2})', cpf))
