"""
Learning about quantifiers:
* - 0 or n
+ - 1 or n
? - 0 or 1
{n}
{min,max}
"""
import re

text = """
João trouxe flores para sua amada namorada em 10 de janeiro de 1970.
Maria era o nome dela;


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão
de queijo.
Não canso de ouvir a Maria:
"Jooooooooãoooooooo, o café tá prontinho aqui. Veeemm"!
Jã
Jão
Joã
"""

print(re.findall(r'jo+ão+', text, flags=re.I))
print(re.findall(r'jo*ão*', text, flags=re.I))
print(re.findall(r'jo?ão?', text, flags=re.I))
print(re.findall(r'jo{1,}ão{1,4}', text, flags=re.I))
print(re.findall(r'j[ao]+ão{1,4}', text, flags=re.I))
