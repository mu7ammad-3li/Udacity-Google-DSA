
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
- [*] Define **daysBetweenDates** To Give Approximate Answers using 

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
    if (isBeforeDate1(Y1,M1,D1,Y2,M2,D2)):

        print ("Dayes In Betwwen = ",daysBetwwnDates(Y1,M1,D1,Y2,M2,D2))
    else : 
        print("Invalid Date")

```




## if __name__ == "__main__"


## System arguments 


```python 

import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

```
```bash 
$ python3 sysarg.py 1 2 3 
Total arguments passed =  4

```

### Argv[0]
argv[0] Contains The name of The Script 

```python 
print("\nName of Python script:", sys.argv[0])
```
```bash 
    Name of Python script: sysarg.py
```

```python 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

```

The end parameter in the print function is used to add any string. At the end of the output of the print statement in python. By default, the print function ends with a newline. Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline.

```bash 
Arguments passed : 1 2 3 
```

```python 
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)
```
```bash 
Result: 6
```

Script : 
```python 

import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)
```

```bash 
Total arguments passed: 4

Name of Python script: sysarg.py

Arguments passed: 1 2 3 

Result: 6
```

