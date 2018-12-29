from random import randint

"""
This code is to calculate random integer between 1 and 7 if we know a function called rand5
which can generate a random integer between 1 and 5
"""

def rand5():
    return randint(1,5)

def rand7():
    while (True):
        result = (rand5() - 1) + (5 * (rand5() - 1))
        if (result <= 20):
            break

    result = 1 + (result % 7)
    return result

"""
Main function
"""
def main():
    x = 0
    outDict = {}
    while x <= 100:
        x += 1
        num = rand7()
        if num not in outDict:
            outDict[num] = 1
        else:
            outDict[num] +=1
    print("outDict is :%s"%outDict)

if __name__ == "__main__":
    main()

