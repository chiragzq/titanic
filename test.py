import csv

class Passenger:
    def __init__(self, data):
        self.id = int(data[0])
        self.survived = int(data[1])
        self.Pclass = int(data[2])
        self.name = data[3]
        self.gender = data[4]
        self.age = (int(float(data[5])) if data[5] != "" else -1)


    def __str__(self):
        return str(self.id) + " " + str(self.survived) + " " + self.name


passengers = []

f = open("train.csv", "r")
reader = csv.reader(f)
next(reader, None)
for row in reader:
    passengers.append(Passenger(row))
f.close()


classWeight = 0.5
genderWeight = 0.1
ageWeight = 0.5
ages = [0, 3, 16, 45, 60, 80]
ageScale = 160000
ageCurveDenom = 0

def ageCurveNone(age):
    return -(age-ages[0]) * (age-ages[1]) * (age-ages[2]) * (age-ages[3]) * (age-ages[4]) * (age-ages[5])

def findConst():
    maxV = 0
    increment = 0.1
    for i in range(0,int(ages[3] / increment)):
        if (abs(ageCurveNone(i * increment)) > maxV):
            maxV = abs(ageCurveNone(i * increment))
    return maxV

def ageCurve(age):
    return ageCurveNone(age) / ageCurveDenom

def predictSurvived(passenger):
    surviveChance = 0
    surviveChance += genderWeight if passenger.gender == "female" else -genderWeight
    surviveChance += (passenger.Pclass - 2) * -classWeight
    surviveChance += (ageCurve(passenger.age) * ageWeight if passenger.age != -1 else 0)

    return surviveChance > 0

def testSolution():
    total = 0
    for passenger in passengers:
        if(passenger.survived == predictSurvived(passenger)):
            total+=1
    print(str(total) + "/" + str(len(passengers)))
ageCurveDenom = findConst()
testSolution()
print(findConst())

string = ""
x=0
for passenger in passengers:
    string = string + str(passenger.survived) + " "
    x+=1
print(string + "1 1 1")
print(x)
