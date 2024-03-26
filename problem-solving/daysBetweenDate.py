import sys
from nextdayV1 import nextDay,inputPrinting

def daysBetwwnDates(Y1,M1,D1,Y2,M2,D2):
    """This Script Assumes The First Date In Argument Is The Oldest
    """
    print("daysBetwwnDates()")
    print(daysBetwwnDates.__doc__)
    daysInBetween= 0
    while(not(Y1==Y2 and M1==M2 and D1==D2)):
        result =nextDay(Y1,M1,D1)
        print (result)
        daysInBetween +=1
        Y1 = int(result[0])
        M1 = int(result[1])
        D1 = int(result[2])
    return daysInBetween

    
if __name__ == "__main__":
    inputPrinting(sys.argv)
    Y1 = int(sys.argv[1])
    M1 = int(sys.argv[2])
    D1 =int (sys.argv[3])
    Y2 = int(sys.argv[4])
    M2 = int(sys.argv[5])
    D2 =int (sys.argv[6])  
    print ("Dayes In Betwwen = ",daysBetwwnDates(Y1,M1,D1,Y2,M2,D2))


