def reverseSting(text):
    index = -1
    print(len(text))
    # Loop from last index until half of the index
    for i in range(len(text) - 1, int(len(text) / 2), -1):

        # match character is alphabet or not
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text

input = "Apples & Ban@na";
#       annaBs & elp@pA
# Driver code
string = input
print("Input string: ", string)
string = reverseSting(list(string))
print("Output string: ", "".join(string))
