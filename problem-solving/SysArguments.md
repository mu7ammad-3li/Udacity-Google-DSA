
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

