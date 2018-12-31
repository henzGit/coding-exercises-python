"""
Given a 8x8 chess board what is the cumulative probability that next move
will fall in the chess board.
"""

"""
@:param initPos [X0, Y0] array containing initial position
@:param n int number of next moves 
"""
def calcProbNextMoveWithinChessBoard(initPos, n):
    queue = [initPos]

    nextMoves = [
                        [1, 2], [1, -2], [-1, 2], [-1, -2],
                        [2, 1], [2, -1], [-2, 1], [-2, -1]
                 ]

    for i in range(n):
        for j in range(len(queue)):
            currPos = queue.pop(0)
            for nextMove in nextMoves:
                nextXPos = currPos[0] + nextMove[0]
                nextYPos = currPos[1] + nextMove[1]

                # if x position or y position is out of boundaries, continue to nextMove
                if nextXPos < 0 or nextXPos > 7 or nextYPos < 0 or nextYPos > 7:
                    continue

                nextPos = [nextXPos, nextYPos]
                if nextPos not in queue:
                    queue.append(nextPos)

    return len(queue)/(8**n)

"""
Main function
"""
def main():
    prob =   calcProbNextMoveWithinChessBoard([0, 0] ,  10)
    print("prob: %s" %prob)

if __name__ == "__main__":
    main()

