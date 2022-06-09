import string
from fnmatch import translate

print(string.ascii_lowercase)

abc = string.ascii_lowercase
print(abc)

print(abc[5: ] + abc [ :5])
s = "hello"
trans = abc[5: ] + abc[ :5]
print(s.translate(str.maketrans(abc, trans)))
print('mjqqt'.translate(str.maketrans(trans, abc)))

