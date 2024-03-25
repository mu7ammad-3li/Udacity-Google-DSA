
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

