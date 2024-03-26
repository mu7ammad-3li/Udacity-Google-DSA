
# Problem Solving 

## nextDay Problem 


### version One 

```python 
import sys


def nextDay(year,month,day):
    """ This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    """
    if (day<30):
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
    print (nextDay.__doc__)

    print("Next day is :",result[0],result[1],result[2])
```

```bash 

$ python3 nextdayV1.py 1995 10 01
---------------------------------
Arguments : 1995 10 01 

 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
Next day is : 1995 10 2
```
### What Should We Do Next ? 

- [ ] Refine **nextDay** To Work Correctly For real months
- [X] Define **daysBetweenDates** To Give Approximate Answers using 

**nextDay** Procedure 

> Both Answers Are Vaild Pathes But Its better To : 
Define **daysBetweenDates** To Give Approximate Answers using **nextDay** Procedure 


## daysBetweenDates

Using The simpler **nextDay** procedure We are Going To Emplemnt **dayesBetweenDates**

```python
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

```

```bash 
$ python3 daysBetweenDate.py 1995 10 01 1995 10 10
--------------------------------------------------
daysBetwwnDates()
This Script Assumes The First Date In Argument Is The Oldest
    
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 2)
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 3)
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 4)
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 5)
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 6)
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 7)
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 8)
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 9)
nextDay()
 This Version Of the program is not logically Correct 
    - It Assumes Every Month is 30 Days 
    
(1995, 10, 10)
Dayes In Betwwen =  9
```


### Refining daysBetwwenDates 

A useful approach Is to write a helper Function **isDateBefore**
That return True Or false If **Date1** Is Before **Date2**

```
**daysBetwwenDate**

daysInBetwwen = 0 
while (isDateBefore(Date1,Date2))
    DaysInBetween +=1
    Date1=nextDay(Date1)
    return DaysInBetween
```
```
**isDateBefore**

if(Y2>Y1)
    return True
else if (Y2==Y1):
    if(M2>M1)
        return True
    else if (M2==M1):
        if (D2>D1)
            return True
        else:
            return False
    else:
        return False
else:
    return False

```
```python 
# isBeforeDate1 Helper Function emplementaion
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
            print("Second Date Is Invalid")
            return False
    else:
        print("Second Date Is Invalid")
        return False
    
```
```python 
#daysBetwwnDates Refactoring 
def daysBetwwnDates(Y1,M1,D1,Y2,M2,D2):
    """This Script Assumes The First Date In Argument Is The Oldest
    """
    print("daysBetwwnDates()")
    print(daysBetwwnDates.__doc__)
    daysInBetween= 0
    while(isBeforeDate1(Y1,M1,D1,Y2,M2,D2)):
    #...
    #...

```

```python 
#Main Function Refactoring 
if __name__ == "__main__":

    if (isBeforeDate1(Y1,M1,D1,Y2,M2,D2)):

        print ("Dayes In Betwwen = ",daysBetwwnDates(Y1,M1,D1,Y2,M2,D2))
    else : 
        print("Invalid Date")

```

#### Refactored 
```python 
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
            print("Second Date Is Invalid")
            return False
    else:
        print("Second Date Is Invalid")
        return False
    


def daysBetwwnDates(Y1,M1,D1,Y2,M2,D2):
    """This Script Assumes The First Date In Argument Is The Oldest
    """
    print("daysBetwwnDates()")
    print(daysBetwwnDates.__doc__)
    # throws an exception when  Date 2 Is less than Date 1 
     assert not isBeforeDate1(Y2,M2,D2,Y1,M1,D1)
    daysInBetween= 0
    while(isBeforeDate1(Y1,M1,D1,Y2,M2,D2)):
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

```

## Real World Problem 
### What to Do next ? 

- [x] write stub **daysInMonth(Year,Month)** that Always Return 30 
- [x] Mdifify **nextDay()** to use **daysInMonth(Year,Month)**
- [x] Test nextDay() using stub **daysInMonth(Year,Month)**

At This Point We did not change the output from the last program we just re-structured the code for the next steps 

Next : 

- [ ] Modify **daysInMonth(Year,Month)**  to be correct except for leep years 
- [ ] Test Again nextDay() using stub **daysInMonth(Year,Month)**
- [ ] write isLeapYear(Year)
- [ ] test isLeapYear(Year) separately
- [ ] modify daysInMonth(Year,Month) to account For leap years
- [ ] Test daysBetweenDates() for all Cases 

