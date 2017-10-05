import re
match = re.search(r'PY.*? N',"PYannhjdcgbhdgfNdN")
print(match.group(0))