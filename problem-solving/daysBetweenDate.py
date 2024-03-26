import sys
from nextdayV1 import nextDay,inputPrinting

def isBeforeDate1(Y1,M1,D1,Y2,M2,D2):
    if(Y2>Y1):
        return True
    elif(Y2==Y1):
        if(M2>M1):
            return True
        elif(M2==M1):
            if(D2>D1):
                return True
            else:
                return False
    else:
        return False
    


def daysBetwwnDates(Y1,M1,D1,Y2,M2,D2):
    """This Script Assumes The First Date In Argument Is The Oldest
    """
    #print("daysBetwwnDates()")
    #print(daysBetwwnDates.__doc__)
    assert not isBeforeDate1(Y2,M2,D2,Y1,M1,D1)
    daysInBetween= 0
    while(isBeforeDate1(Y1,M1,D1,Y2,M2,D2)):
        result =nextDay(Y1,M1,D1)
        #print (result)
        daysInBetween +=1
        Y1 = int(result[0])
        M1 = int(result[1])
        D1 = int(result[2])
    return daysInBetween

if __name__ == "__main__":
    #inputPrinting(sys.argv)
    Y1 = int(sys.argv[1])
    M1 = int(sys.argv[2])
    D1 =int (sys.argv[3])
    Y2 = int(sys.argv[4])
    M2 = int(sys.argv[5])
    D2 =int (sys.argv[6])  
    print(f"Starting From {Y1}-{M1}-{D1} to {Y2}-{M2}-{D2}")
    print ("Dayes In Betwwen = ",daysBetwwnDates(Y1,M1,D1,Y2,M2,D2))
        

