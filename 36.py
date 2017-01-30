def val(a):
    if (a == '0'):
        return 0
    elif (a == '1'):
        return 1
    elif (a == '2'):
        return 2
    elif (a == '3'):
        return 3
    elif (a == '4'):
        return 4
    elif (a == '5'):
        return 5
    elif (a == '6'):
        return 6
    elif (a == '7'):
        return 7
    elif (a == '8'):
        return 8
    else:
        return 9

def isValidSudoku(board):
        tag_x = []
        tag_y = []
        tag = []
        for i in range(0,10):
            a = []
            b = []
            c = []
            for j in range(1,10):
                a += [0]
                b += [0]
                c += [0]
            tag_x += [a]
            tag_y += [b]
            tag += [c]

        for i in range(0,9):
            for j in range(0,9):
                if (board[i][j] != '.'):
                    if (tag_x[val(board[i][j])][i] == 1):
                        return bool(0)
                    else:
                        tag_x[val(board[i][j])][i] = 1
                    if (tag_y[val(board[i][j])][j] == 1):
                        return bool(0)
                    else:
                        tag_y[val(board[i][j])][j] = 1
                    tmp = int(i/3)*3+int(j/3)
                    if (tag[val(board[i][j])][tmp] == 1):
                        return bool(0)
                    else:
                        tag[val(board[i][j])][tmp] = 1
        return bool(1)

a =[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print(isValidSudoku(a))
