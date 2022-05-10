#WAP to count frequency of words
import pprint

def freq_words():
    str = input("Enter a String: ")
    li = str.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)

freq_words()

#another way to count words.. here using setdefault() method
def setDefaultTest():
    str = "python is a dynamic is a type a language"
    li = str.split()
    d = {}

    for i in li:
        d.setdefault(i, 0)
        d[i] = d[i]+1
    pprint.pprint(d)

setDefaultTest()