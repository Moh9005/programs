import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
z= '{"model":"civic", "year": "2000"}'
# parse x:
y = json.loads(x)
m= json.loads(z)
# the result is a Python dictionary:
print(y["age"], m["year"])



# a Python object (dict):
x = { "name": "John", "age": "30", "city": "New York"}

'''# convert into JSON:
y = json.dumps(x["age"])

# the result is a JSON string:
print(y)'''



x = {"name": "John","age": 30, "married": True, "divorced": False, "children": ("Ann","Billy"),"pets": None,
     "cars": [{"model": "BMW 230", "mpg": 27.5},{"model": "Ford Edge", "mpg": 24.1}]}


json.dumps(x, indent=4)
print(json.dumps(x))