column1 = []
column2 = []

with open("1/data.txt", "r") as file:
    for line in file:
        values = line.split()  
        column1.append(int(values[0]))
        column2.append(int(values[1]))

def calcDistance(list1, list2):
    totalDistance = 0
    list1.sort()
    list2.sort()
    for x, y in zip(list1, list2):
        totalDistance += abs(x - y)
    print (totalDistance)

calcDistance (column1, column2)

                
        