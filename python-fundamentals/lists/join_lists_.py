# L1 = [10,20,30,40]
# L2 = ['ten', 'twenty', 'thirty', 'forty']
# print(L1 + L2)

# L1 = [36, 24, 3]
# L2 = [84, 5, 81]
# joined_list = [item for sublist in [L1, L2] for item in sublist]
# print(joined_list)
# joined_list = [item for sublist in [L1, L2] for item in sublist]
# print(joined_list)
# joined_list = [item for sublist in [L1, L2] for item in sublist]
# print(joined_list)
# joined_list = [item for sublist in [L1, L2] for item in sublist]
# print(joined_list)
# joined_list = [item for sublist in [L1, L2] for item in sublist]
# print(joined_list)


# list1 = ['Fruit', 'Number', 'Animal']
# list2 = ['Apple', 5, 'Dog']
# for item in list2:
#     list1.append(item)
# print(list1)
# for item in list2:
#     list1.append(item)
# print(list1)
list1 = [10, 15, 20]
list2 = [25, 30, 35]
list1.extend(list2)
print(list1)

print(dir([]))
print(help([].append))