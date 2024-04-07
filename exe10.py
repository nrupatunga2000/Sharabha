# reate a new list from two list using the following condition
#
# Given two list of numbers, write a program to create a new list
# such that the new list should contain odd numbers
# from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

for new_list in list1:
    if new_list % 2 ==0:
        list3.append(new_list)
for new_list2 in list2:
    if new_list2 %2 !=0:
        list3.append(new_list2)
print(list3)



