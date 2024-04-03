#Check if the first and last number of a list is the same
#Given list: [10, 20, 30, 40, 10]
# result is True
#
# numbers_y = [75, 65, 35, 75, 30]
# result is False

numbers = [10,20,30,10]
xyz = len(numbers)-1
if numbers[xyz] == numbers[0]:
    print("true")
else:
    print("false")
