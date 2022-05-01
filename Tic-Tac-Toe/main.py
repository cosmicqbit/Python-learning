def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('0' if zState[0] else 0)
    one = 'X' if xState[1] else ('0' if zState[1] else 1)
    two = 'X' if xState[2] else ('0' if zState[2] else 2)
    three = 'X' if xState[3] else ('0' if zState[3] else 3)
    four = 'X' if xState[4] else ('0' if zState[4] else 4)
    five = 'X' if xState[5] else ('0' if zState[5] else 5)
    six = 'X' if xState[6] else ('0' if zState[6] else 6)
    seven = 'X' if xState[7] else ('0' if zState[7] else 7)
    eight = 'X' if xState[8] else ('0' if zState[8] else 8)

    print(f"{zero} | {one} | {two} |")
    print(f"--|---|---|")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---|")
    print(f"{six} | {seven} | {eight} |")

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X & 0 for O
    print("Welcome to Tic Tac Toe Game!")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value\n"))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value\n"))
            zState[value] = 1
        turn = 1 - turn