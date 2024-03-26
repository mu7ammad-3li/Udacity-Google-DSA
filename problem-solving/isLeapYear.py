
#TODO: write isLeapYear(Year) -- Done

def isLeapYear(Year):
    if ((Year%4==0 and not (Year %100==0)) or Year %400==0 ):
        #print (f"Year {Year} is Leep Year")
        return True 
    else:
        return False 
