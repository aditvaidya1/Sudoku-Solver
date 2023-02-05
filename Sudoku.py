board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


def solve_board(b):
    find_emp = find_empty(b)
    if not find_emp:
        return True
    else:
        row, col = find_emp

    for i in range(1,10):
        if valid_num(b, i, (row, col)):
            b[row][col] = i

            if solve_board(b):
                return True

            b[row][col] = 0

    return False


def valid_num(b, num, pos):
 
    for i in range(len(b[0])):                            # Here i check the row 
        if b[pos[0]][i] == num and pos[1] != i:
            return False

   
    for i in range(len(b)):                                #here i check column
        if b[i][pos[1]] == num and pos[0] != i:
            return False

                                                            # Checking the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("__________________________ ")
            print()

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 4:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)                                  

    return None

print_board(board)
solve_board(board)
print("\n")
print("*********OUTPUT**********")
print("\n")
print_board(board)