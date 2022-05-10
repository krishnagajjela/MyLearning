import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

print(id(old_list[0][0]))
print(id(new_list[0][0]))

old_list.append([4, 4, 4])
old_list[1][0] = 'BB'
print(old_list)
print(new_list)