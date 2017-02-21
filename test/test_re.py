import re

pattern = re.compile(r'h\+o')
match = pattern.match('hello world')
print match.group()
