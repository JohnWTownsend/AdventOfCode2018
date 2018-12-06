
class FabricCut:
    def __init__(self, line):
        attributeArray = line.split(" ")
        self.Id = self.getId(attributeArray[0])
        self.LeftOffset, self.TopOffset = self.getOffset(attributeArray[2])
        self.Width, self.Height = self.getDimensions(attributeArray[3])
    def print(self):
        print(f'ID: {self.Id} | Offset: {self.LeftOffset}, {self.TopOffset} | Dimensions: {self.Width}X{self.Height}')
    
    def getId(self, idString):
        return idString.replace("#", "")

    def getOffset(self, offsetString):
        values = offsetString.replace(":","").split(",")
        return int(values[0]), int(values[1])

    def getDimensions(self, dimensionsString):
        values = dimensionsString.split("x")
        return int(values[0]), int(values[1])

class Fabric:
    def __init__(self, cuts):
        self.Width = maxWidth(cuts)
        self.Height = maxHeight(cuts)
        self.Array = self.constructArray()
        self.addCutsToArray(cuts)
        
    def constructArray(self):
        arr = []
        for row in range(self.Height):
            arrRow = []
            for col in range(self.Width):
                arrRow.append(".")
            arr.append(arrRow)
        return arr

    def addCutsToArray(self, cuts):
        for x in cuts:
            left = x.LeftOffset
            right = x.Width + x.LeftOffset
            top = x.TopOffset
            bottom = x.TopOffset + x.Height
            for row in range(top, bottom):
                for col in range(left, right):
                    if(self.Array[row][col] == "."):
                        self.Array[row][col] = 1
                    elif(self.Array[row][col] == 1):
                        self.Array[row][col] = "X"

    def getTotalCutArea(self):
        total = 0
        for row in range(self.Height):
            for col in range(self.Width):
                if(self.Array[row][col] == "X"):
                    total = total + 1
        return total

    def printArray(self):
        for row in range(self.Height):
            for col in range(self.Width):
                print(f' {self.Array[row][col]} ', end='')

def maxWidth(cuts):
    maxWid = 0
    for cut in cuts:
        proposedWidth = cut.Width + cut.LeftOffset
        if(proposedWidth > maxWid):
            maxWid = proposedWidth
    return maxWid

def maxHeight(cuts):
    maxHeight = 0
    for cut in cuts:
        proposedWidth = cut.Height + cut.TopOffset
        if(proposedWidth > maxHeight):
            maxHeight = proposedWidth
    return maxHeight




inputFile = open("day3Input.txt")
textInput = inputFile.read()
readLines = textInput.splitlines()
print(readLines)

FabricCuts = []
for line in readLines:
    fabricCut = FabricCut(line)
    FabricCuts.append(fabricCut)
    fabricCut.print()

fabric = Fabric(FabricCuts)
print(fabric.getTotalCutArea())