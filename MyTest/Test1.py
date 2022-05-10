import re

testStr= "10vvbfb20FFDSFD70"
vals = re.findall("\d+", testStr)
# or
# vals = re.findall("[0-9]+", testStr)
sum1 = 0
for i in vals:
    sum1 = sum1 + int(i)

print(sum1)

# def reMulVal():
#     ol = [1,7, 5,4,2,]
#     sum = 6
#     p = {}
#     for i in ol:
#         for j in ol:
#             print(i, j)
#             temp = i+j
#             if (temp == sum):
#                 p.update(i, j)
#     return p
#
# x = reMulVal()
# print(x)
# #
# # ol.sort()
# # length = len(ol)
# # d = {}
# # for i in range(0, length+1):
# #     if(ol[i]+ol[i+1] == 6):
# #       d.update(ol[i],ol[i+1])
# #
# # print(d)
