"""
https://www.hackerrank.com/challenges/fibonacci-modified/problem
"""
def fibonacciModified(t1, t2, n):
    if n == 1:
        return t1
    elif n == 2:
        return t2
    else:
        for i in range(n-2):
            t3 = t1 + (t2*t2)
            t1 = t2
            t2 = t3
        return t3

"""
Main function
"""
def main():
    t1 = 0
    t2 = 1
    n = 5
    result = fibonacciModified(t1, t2, n)
    print(result)
if __name__ == "__main__":
    main()

