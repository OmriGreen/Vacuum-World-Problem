from vacuumCheck import vacuumCheck
import statistics

class main:
    
    scoreList = []
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i == 0:
                    iLoc = "A"
                    iString = "Starting in A |"
                else:
                    iLoc = "B"
                    iString = "Starting in B |"
                if j == 0:
                    jString = " A is clean |"
                else:
                    jString = " A is dirty |"
                if k == 0:
                    kString = " B is clean |"
                else:
                    kString = " B is dirty |"
                tempVac = vacuumCheck(iLoc, j, k)
                value = int(tempVac.cost)
                print(iString + jString + kString + " performance score is "+str(value))
                scoreList.append(value)
    print("The average performance score is " +str(statistics.mean(scoreList)))
a = main()