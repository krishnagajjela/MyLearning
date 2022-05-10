def missing_number(a):
    a.sort()
    n = a[-1]
    sum1 = 0
    total = n*(n+1)//2 #summarization method return sum of natural number

    sum1 = sum(a)
    print(total)
    print(sum1)
    res = total - sum1
    print("Missing Number is: ", res)

a = [7,2,3,6,1,5]
missing_number(a)