color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print("Original set elements:")
print(color_list_1)
print(color_list_2)

print("\nUnique colors from both the lists:")
# print(color_list_1.difference(color_list_2))
print(color_list_1-color_list_2)



print("\nDifferent of color_list2 and color_list1:")
# print(color_list_2.difference(color_list_1))
print(color_list_2-color_list_1)
