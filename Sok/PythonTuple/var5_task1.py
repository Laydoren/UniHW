with open('INPUT_task1.txt', 'r') as filein:
    with open('OUTPUT_task1.txt', 'w') as fileout:

        row, col = map(int, filein.readline().split())

        table = [list(filein.readline().strip()) for i in range(row)]

        dot_row = [i for i in range(row) for j in range(col) if table[i][j] == '*']
        dot_col = [j for i in range(row) for j in range(col) if table[i][j] == '*']


        if dot_row:
            for i in range(min(dot_row), max(dot_row) + 1):
                for j in range(min(dot_col), max(dot_col) + 1):
                    table[i][j] = '*'

        for row_line in table:
            fileout.write(''.join(row_line) + '\n')