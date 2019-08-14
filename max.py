## List to find the maximum and minimum number in a list and find their difference

listA = [25,3,34,65,87,98,2,12,-56,34,6]

#set counter anr refNumber
counter = 0
refMin = listA[0]
refMax = listA[0]

# Loop as long as the counter is less than the length of list
while counter < len(listA):
    if listA[counter] < refMin:
        refMin = listA[counter]

        print("Smallest number so far", refMin)
    elif listA[counter] > refMax:
        refMax = listA[counter]
        print("Largest number so far", refMax)
    counter += 1
print("Difference between the max and min is, :" , refMax - refMin)