"""
Learning more about greedy and lazy quantifiers and their usage
"""
import re

text = """
<p>tag 1</p> <p>tag 2</p> <p>tag 3</p> <div>tag 4</div>
"""
#ambiguous (greedy, gets the max information possible)
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', text))

#lazy (non-greedy, gets the minimum information possible)
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text))
