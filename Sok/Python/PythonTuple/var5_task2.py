with open('INPUT_task2.txt', 'r') as filein:
    with open('OUTPUT_task2.txt', 'w') as fileout:
        num_table = int(filein.readline())

        for table_num in range(1, num_table + 1):
            nice = True
            row, col = map(int, filein.readline().split())
            table = [list(map(int, filein.readline().split())) for i in range(row)]

            for i in range(row - 1):
                for j in range(col - 1):
                    box_check = table[i][j] + table[i + 1][j] + table[i][j + 1] + table[i + 1][j + 1]
                    if box_check == 0 or box_check == 4:
                        nice = False

            if nice:
                fileout.write(f"Таблица номер {table_num} симпатичная\n")
            else:
                fileout.write(f"Таблица номер {table_num} несимпатичная\n")