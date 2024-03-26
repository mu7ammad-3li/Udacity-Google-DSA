import sys
from daysInMonth import daysInMonth

def nextDay(year,month,day):
    """ This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    """
    print("nextDay()")
    print (nextDay.__doc__)

    # Mdifify nextDay()to use daysInMonth(Year,Month) -- done
    # Test nextDay() using stub daysInMonth(Year,Month) -- done 
    Days = daysInMonth(year,month)
    if (day<Days):
        return year,month,day+1
    else:
        if (month<12):
            return year,month+1,1
        else:
            return year+1,1,1

def inputPrinting(li):
        n = len(li)
        print ("Arguments : ",end="")
        for i in range(1,n):
            print(li[i],end=" ")
        print("\n")

if __name__ == "__main__":

    inputPrinting(sys.argv)
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day =int (sys.argv[3]) 
    
    result = nextDay(year,month,day)
    print("Next day is :",result[0],result[1],result[2])