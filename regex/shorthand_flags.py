"""
Learning more about shorthand and flags and their usage

Shorthands:
    \w      : [a-zA-Z0-9À-ú_]
    \w, re.A: [a-zA-Z0-9_]
    \W      : ~[a-zA-Z0-9À-ú_]
    \W, re.A: ~[a-zA-Z0-9_]
    \d      : [0-9]
    \D      : ~[0-9]
    \s      : [ \r\n\f\n\t]
    \S      : ~[ \r\n\f\n\t]
    \b      : border
    \B      : not border

Flags:
    re.I: ignore case
    re.A: ASCII character
    re.M: multiline - ^ $
    re.S: dotall
"""
import re

text = """
João trouxe flores para sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão
de queijo.
Não canso de ouvir a Maria:
"Jooooooooãoooooooo, o café tá prontinho aqui. Veeemm"!
"""

# print(re.findall(r"\w+", text))
# print(re.findall(r"\w+", text, flags=re.A))
# print(re.findall(r"\W+", text))
# print(re.findall(r"\W+", text, flags=re.A))

# print(re.findall(r"\d+", text, flags=re.I))
# print(re.findall(r"\D+", text, flags=re.I))

# print(re.findall(r"\s+", text, flags=re.I))
# print(re.findall(r"\S+", text, flags=re.I))

# print(re.findall(r"\be\w+", text, flags=re.I))
# print(re.findall(r"\w+e\b", text, flags=re.I))
# print(re.findall(r"\b\w{4}\b", text, flags=re.I)) #all 4 letters words

text = """
012.345.678.901-23 ABC
456.789.012.345-67 DEF
890.123.456.789-01
"""

# print(re.findall(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$", text, flags=re.M))

text2 = 'O joão gosta de folia \n E adora ser amado'

print(re.findall(r"^o.*o$", text2, flags=re.I | re.S))
