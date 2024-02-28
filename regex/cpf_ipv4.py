"""
Applying CPF and IPV4 validation with regex
"""
import re

cpf = '205.468.598-89'
cpf_reg_exp = re.compile(r'^\d{3}.\d{3}.\d{3}-\d{2}$')
print(cpf_reg_exp.search(cpf))

ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5]| # 250-255
            2[0-4][\d]| #200-249
            1[\d]{2}| #100-199
            [1-9][\d]| #10-99
            [\d] #0-9
        )
        \.
    ){4}
    \b
    $
''', flags=re.VERBOSE)
