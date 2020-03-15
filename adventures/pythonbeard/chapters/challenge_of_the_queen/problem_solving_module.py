import copy

"""
def solve_queens(board_size, current_board=[],  index=0):
    
    if index == board_size:
        return 1
    
    counter = 0
    for i in range(board_size):
        flag = True
        for j in range(index):
            if i == current_board[j] or \
                index - j == i - current_board[j] or \
                index - current_board[j] == j - i:
                flag = False
                break
        if flag:
            counter += solve_queens(board_size, current_board + [i], index + 1)
    return counter
"""
 
def solve_queens(board_size=8, current_board=[],  index=0):
    return sum([solve_queens(board_size, current_board + [i], index + 1) if 
                not any([i == current_board[j] or 
                         index - j == i - current_board[j] or 
                         index - current_board[j] == j - i 
                        for j in range(index)]) 
                else 0 for i in range(board_size)]) if index != board_size else 1



def queens() -> int:
    """
    Solve the queens problem.

    :return: how many queens can be placed on an 8x8 board.
    :rtype: int
    """
    # Your code here:
    return solve_queens()