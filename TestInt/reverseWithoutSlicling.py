def reverse(s):
  str = ""
  for i in s:
    print(i)
    str = i + str
  return str

s = "avc"
print(reverse(s))
