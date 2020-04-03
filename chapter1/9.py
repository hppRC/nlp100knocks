import re
import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

for p in re.finditer(r'[a-zA-Z\']+', s):
    (left, right) = p.span()
    k = right - left
    if k <= 4:
        continue
    partial_str = s[left + 1: right - 1]
    s = s[:left+1] + \
        "".join(random.sample(s[left + 1: right - 1], k - 2)) + s[right-1:]
print(s)
