
rowTotals = list(map(lambda x: 0 if x < 0 else x, [sum(map(lambda x: symbols[x], row)) for row in board]))
colTotals = list(map(lambda x: 0 if x < 0 else x, [sum(map(lambda x: symbols[x], [row[i] for row in board])) for i in range(len(board))]))




def calculate_score_oneline(board): 
    return [max(sum([ {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}[x] for x in r ]), 0) for r in board ], [ max(sum([ {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}[board[x][y]] for x in range(len(board))] ), 0)for y in range(len(board[0]))]