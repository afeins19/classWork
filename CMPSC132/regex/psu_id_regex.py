# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


if re.search('^[+,-]?[.]?\d+$',input()):
    print(True)
else:
    print(False)
