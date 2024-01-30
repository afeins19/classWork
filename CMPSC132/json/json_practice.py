#reffer to sample_text file for the json dict

import json

json_file = open(r'/Users/aaronfeinberg/PycharmProjects/Playground/json/sample_text','r')
student = json.load(json_file)

print(student)

json_file.close()
#using json string
fiesta="""
    {
        "is_lit":true,
        "crowd predisposition":"in trance"
    }
"""


test=json.loads(fiesta)
print(test)

meow={1:True,2:3}
print(json.load(meow))

user={'id':1,'name':'puko'}

user_to_j=json.dumps(user)
print(user_to_j)

