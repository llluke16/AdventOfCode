column1 = []
column2 = []

with open("1/data.txt", "r") as f:
    for line in f:
        val = line.split()  
        column1.append(int(val[0]))
        column2.append(int(val[1]))
                
def calcSimilarity(list1, list2):
    similarityScore = 0
    for a in list1:
        occurences = list2.count(a)
        similarityScore += a * occurences
    print(similarityScore)


calcSimilarity(column1, column2)