"""
This code is to return all sequences of numbers that sum to it given an integer.
(Example: 3 => (1, 2), (2, 1), (1, 1, 1)).
"""

def returnAllSeqGivenAnInteger(integer):
    result = []
    queue = [[]]

    while queue:
        currBaseList = queue.pop(0)
        for num in range(1,10):
            tempList = list(currBaseList)
            tempList.append(num)
            if sum(tempList) == integer:
                result.append(tempList)
                break

            queue.append(tempList)
    return result

"""
Main function
"""
def main():
    result = returnAllSeqGivenAnInteger(5)
    print(result)
if __name__ == "__main__":
    main()

