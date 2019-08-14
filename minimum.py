# To find the lowest numberRef from the list

listA = [9,7,4,5,14,65,85,45,6,2,-1]

#create a counter
#read a reference point to start and call it numberRef

counter = 0
numberRef = listA[0]

# Use a while loop to loop through each integer in the list
while counter<len(listA):
    if listA[counter]<numberRef:
        print("Lowest numberRef so far", numberRef)
        numberRef = listA[counter]
        print("Lowest numberRef has now changed to: ", numberRef)
    counter = counter + 1
    print("Counter is now at: " , counter)
print("Smallest numberRef in the list is : ", numberRef)

## Lazier way to find the min
minimumNum = min(listA)
maximumNum = max(listA)

print("smallest number on list: ", minimumNum)
print("largest number on list: " , maximumNum)

# Also you could use sorting
listA.sort()
print("Smallest using sort: ", *listA[:100])
print(listA[:1])
