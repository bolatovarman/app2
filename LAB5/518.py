import re

s = input()
pattern = input()

escaped = re.escape(pattern)

matches = re.findall(escaped, s)

print(len(matches))