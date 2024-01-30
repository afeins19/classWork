#removes punctuation from a string

import string

s='t../,.,a(s)(t)(y).'
exclude = set(string.punctuation)
s = ''.join(ch for ch in s if ch not in exclude)
print(s)
