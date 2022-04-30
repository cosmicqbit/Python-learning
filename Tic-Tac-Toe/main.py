def printBoard():
    print(f"0 | 1 | 2 |")
    print(f"--|---|---|")
    print(f"3 | 4 | 5")
    print(f"--|---|---|")
    print(f"6 | 7 | 8 |")

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X & 0 for O
    print("Welcome to Tic Tac Toe Game!")
    while(True):
        printBoard()
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value\n"))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value\n"))
            zState[value] = 1
        break