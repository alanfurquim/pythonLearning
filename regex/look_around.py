"""
Learning more about look ahead and look behind and their usage

Positive ahead: (?=text)
Negative ahead: (?!text)

Positive behind: (?<=text)
Negative behind: (?<!text)
"""
import re

text = """
ONLINE	192.168.0.1 GHIJK active
OFFLINE	192.168.0.2 GHIJK inactive
OFFLINE	192.168.0.3 GHIJK active
ONLINE	192.168.0.4 GHIJK active
ONLINE	192.168.0.5 GHIJK inactive
OFFLINE	192.168.0.6 GHIJK active
"""

# Positive lookahead
# print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', text))
# print(re.findall(r'(?=.*[^in]active).+', text))

# Negative lookahead
# print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', text))

# Positive Lookbehind
# print(re.findall(r'(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))

# Negative Lookbehind
print(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))
