import random

class GenerateTriangle:
    def __init__(self):
        self.triangle = [[],[],[]]
        self.numbersToUse = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.numbersUsedInTheSides = []

    def generate(self):
        for side in range(0, 3):
            self.setSideOfTriangle(side)

        return self.triangle, self.numbersToUse

    def setSideOfTriangle(self, row):
        for itemOfSide in range(0, 2):
            numberForTheSide = self.getNumber()
            self.triangle[row].append(numberForTheSide)        
            self.numbersToUse.remove(numberForTheSide)
            
    def getNumber(self):
        while True:
            randomNumber = int(random.uniform(1, 10))
            numberValidation = self.validateNumber(randomNumber)
            if numberValidation:
                self.numbersUsedInTheSides.append(randomNumber)
                return randomNumber
            
    def validateNumber(self, number):         
        if self.numbersUsedInTheSides != [] and self.numbersUsedInTheSides.count(number) == 1:
            return False
        return True    

class TestTriangle:
    def __init__(self,triangle, sidesOfTriangle):
        self.sidesOfTriangle = sidesOfTriangle
        self.triangle = triangle

    def test(self):
        if self.sumAllSides():
            return True
        return False

    def sumAllSides(self):
        sumSide1 = self.sidesOfTriangle[0] + self.triangle[0][0] + self.triangle[0][1] + self.sidesOfTriangle[2]
        sumSide2 = self.sidesOfTriangle[0] + self.triangle[1][0] + self.triangle[1][1] + self.sidesOfTriangle[1]
        sumSide3 = self.sidesOfTriangle[1] + self.triangle[2][0] + self.triangle[2][1] + self.sidesOfTriangle[2]
        
        if sumSide1 == 17 and sumSide2 == 17 and sumSide3 == 17:
            return True

class PrintTriangle:
    def printResult(self, sideOfTriangle, endOfTheEachSide):
        print '\nSolucion al problema: \n'
        print "    ", sideOfTriangle[0]
        print "   ", endOfTheEachSide[0][0], endOfTheEachSide[1][0]
        print "  ", endOfTheEachSide[0][1], "  ", endOfTheEachSide[1][1]
        print " ", sideOfTriangle[1],endOfTheEachSide[2][0], endOfTheEachSide[2][1], sideOfTriangle[2]

def triangle():
        count = 0
        while True:
            count += 1
            triangle, sidesOfTriangle = GenerateTriangle().generate()
            testTriangle = TestTriangle(triangle, sidesOfTriangle).test()

            if testTriangle == True:
                PrintTriangle().printResult(sidesOfTriangle, triangle)
                print("\nNumero de intentos: ", count)
                break
        return True

triangle()
