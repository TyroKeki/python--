import csv
from useful_tools import strtoint_list
from 数独storage import *

def solve_sudoku(board):

    def find_empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i,j
        return None

    def is_valid(board,row,col,num):
        for i in range(9):
            if board[row][i] == num:
                return False

        for i in range(9):
            if board[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row + i][box_col + j] == num:
                    return False

        return True

    def solve(board):
        """递归解决数独（挑战）"""
        empty_pos = find_empty(board)

        if not empty_pos:
            return True

        row, col = empty_pos

        """看不懂回溯方法"""
        for num in range(1,10):
            if is_valid(board,row,col,num):
                board[row][col] = num

                if solve(board):
                    return True

                board[row][col] = 0

        return False

    board_copy = [row[:] for row in board]

    if solve(board_copy):
        return board_copy
    else:
        print("解答失败，似乎没有答案")
        return None

if __name__ == '__main__':

    with open("数独数据输入接口.csv", "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        data = []
        for row in reader:
            data.append(row)

    # data = world_hardest()

    new_data = []
    for row in data:
        new_row = strtoint_list(row)
        new_data.append(new_row)

    for d in new_data:
        print(d)

    solution = solve_sudoku(new_data)

    with open("数独求解结果.csv","w",encoding="utf-8-sig",newline="") as file:
         writer = csv.writer(file)
         writer.writerows(solution)
