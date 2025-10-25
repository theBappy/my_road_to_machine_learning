
# shallow-copy
# import copy
# original_list = [[1,2,3], [4,5,6], [7,8,9]]
# shallow_copied_list = copy.copy(original_list)
# print(shallow_copied_list)
# shallow_copied_list[0][0] = 100
# print(original_list)

# deep copy
# import copy 
# original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# deep_copied_list = copy.deepcopy(original_list)
# print("deep copied list: ", deep_copied_list)
# deep_copied_list[0][0] = 100
# print("deep copied list: ", deep_copied_list)
# print("original list: ", original_list)


# original_list = [1,2,3,4,5]
# copied_list = original_list[1:4]
# print("copied list: ", copied_list)
# copied_list[0] = 200
# print("copied list: ", copied_list)
# print("original list: ", original_list)

# original_list = [1,2,3,4,5]
# copied_list = list(original_list)
# print("copied list: ",copied_list)
# copied_list[0] = 100
# print(copied_list)
# print(original_list)

import copy
original_list = [1,2,3,4,5]
copied_list = copy.copy(original_list)
print(copied_list)
copied_list[0] = 100
print(copied_list)
print(original_list)
