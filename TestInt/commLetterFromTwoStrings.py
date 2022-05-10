#get the common letter from two strings

s1 = "krishna"
s2 = "Sisira"

list_a = list(set(s1) & set(s2))

for i in list_a:
    print(i)

test = ""

for x in list_a:
    test=test+x

print(test)