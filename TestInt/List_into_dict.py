#WAP to convert two list into the dict
keys = [1,2,3]
values = ["one", "two", "three"]

res = dict(zip(keys, values))

print(res)

for i in res.items(): #used to print dict to tuple
    print(i)