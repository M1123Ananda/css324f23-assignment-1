import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.
    for idx in range(1, 9):
        if goal[idx] != board[idx]:
            res += 1
    return res

def h3(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    pos = {1:[0,0], 2:[1,0], 3:[2,0], 4:[0,1], 5:[1,1], 6:[2,1], 7:[0,2], 8:[1,2], 0:[2,2]}

    board, _, _ = s
    col_dis = 0
    row_dis = 0

    for i in range(9):
         
         #check row disalignment
         if goal[i] != board[i]:
             if pos[goal[i]][0] != pos[board[i]][0]:
                 row_dis += 1

         #check column disalignment
         if goal[i] != board[i]:
             if pos[goal[i]][1] != pos[board[i]][1]:
                 col_dis += 1
    
    total = row_dis + col_dis
    return total

    # Sum of column and row distance from goal
    # goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    # pos = {1:[0,0], 2:[1,0], 3:[2,0], 4:[0,1], 5:[1,1], 6:[2,1], 7:[0,2], 8:[1,2], 0:[2,2]}
    # distance = []

    # board, _, _ = s

    # for i in range(9):
    #     if goal[i] != board[i]:


    #        distance.append(abs(( pos[board[i]][0] - pos[goal[i]][0] )) + abs(( pos[board[i]][1] - pos[goal[i]][1] )))
        



    # summed = sum(distance)
    #return summed