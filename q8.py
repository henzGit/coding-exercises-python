"""
This question is to create queue using two stacks
https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
"""
import sys

queue = []

"""
Main function
"""
def main():
    F = sys.stdin
    # Read first line
    nbrQueries = int(F.readline())
    while nbrQueries > 0:
        query = F.readline()
        # print front of queue
        if query == "3\n" or query == "3":
            if len(queue) > 0:
                print(queue[0])
        # deque 1 element from queue
        elif query == "2\n" or query == "2":
            if len(queue) > 0:
                queue.pop(0)
        # enqueue 1 element
        else:
            queue.append(int(query.split(" ")[1]))
        nbrQueries -= 1

if __name__ == "__main__":
    main()

