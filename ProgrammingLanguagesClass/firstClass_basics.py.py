#print("Hello World")
# this is a comment line
""" this is a multiple comment line"""

a = 10
print(a)

a="hello"
print(a)
a,b,c = 10,15,26
print(a,b,c,"\n")

a=b=c = "turkey"
print("the value is a: ",a)
print("the value is b: ",b)
print("the value is c: ",c)

import keyword
print(keyword.kwlist)

a=5
print(a, " is of type ",type(a))

a=2.0
print(a, " is of type ",type(a))

a="2.0"
print(a, " is of type ",type(a))

a=1+2j
print(a, " is of type ",type(a))
print("\n")



str = "hi from turkey!"
print(str)
print(str[0])
print(str[1:5])
print(str[3:])
print(str * 2)
print(str+" TEST")
print(str[3:].strip())

print("\n LIST")
lists=['onur',777,2.23,'yilmaz',20.8]
tinyList = [778,'onur']
print(lists)
print(lists[0])
print(lists[1:3])
print(lists[2:])
print(lists * 2)
print(tinyList*2)
print(lists+tinyList)

print("\n TUPLE") #list but readonly, cannot be updated
tuples=('onur',777,2.23,'yilmaz',20.8)
tinyTuple = (778,'onur')
print(tuples)
print(tuples[0])
print(tuples[1:3])
print(tuples[2:])
print(tuples * 2)
print(tinyTuple*2)
print(tuples+tinyTuple)


print("\n DICT")
dicts={}
dicts['one'] = "This is one"
dicts[2] = "This is two"

dicts2 = {'name':'onur', 'code':656,'dept':'IT'}

print(dicts['one'])
print(dicts[2])
print(dicts)
print(dicts2)
print(dicts2.keys())
print(dicts2.values())


print("\n IF ELIF")
a=200
b=33

if b>a:
    print("b is bigger than a.")
elif a==b:
    print("b and a are equals.")
else:
    print("a is bigger than b")

c = 500

if a>b or a>c:
    print("At least one of the conditions is True")


print("\n FOR LOOP")
companies=["apple","microsoft","facebook"]
for x in companies:
    print(x)
for x in "apple":
    print(x)


for x in companies:
    print(x)
    if x == "microsoft":
        break


for x in companies:
    if x=="apple":
        continue
    print(x)

for i in range(5):
    print(i)




