import sys
def sp_round(cash):
    if(cash>=1000000000000):
        c = round(cash/1000000000000,3)
        return(str(c)+"T")
    elif(cash>=1000000000):
        c = round(cash/1000000000,3)
        return(str(c)+"B")
    elif(cash>=1000000):
        c = round(cash/1000000,3)
        return(str(c)+"M")
    elif(cash>=1000):
        c = round(cash/1000,3)
        return(str(c)+"K")
    else:
        return(str(round(cash,2)))
def compound():
    while(True):
        try:
            cash = float(input("Initial investment = $"))
            break
        except Exception as e:
            print("Invalid input")
    while(True):
        try:
            growth = float(input("Year-over-year growth = %"))
            break
        except Exception as e:
            print("Invalid input")
    while(True):
        try:
            years = float(input("Number of years = "))
            break
        except Exception as e:
            print("Invalid input")
    result = cash*(((1+(growth/100))**years))
    result = sp_round(result)
    print("Result: $"+result)
compound()
while(True):
    Yn = input("Continue? (Y/n) ")
    if(Yn=="Y"):
        compound()
    elif(Yn=="n"):
        sys.exit()
    else:
        print("Invalid response")
