def main():
    num1,num2=getInput()
    result=calMulnSum(num1,num2)
    print(f"The result is {result}")

def getInput():
    n1 = int(input("what's the number1?"))
    n2 = int(input("what's the number2?"))
    return (n1,n2)

def calMulnSum(no1,no2):
    if (no1*no2 <= 1000):
        return (no1*no2)
    else:
        return(no1+no2)
    
main()