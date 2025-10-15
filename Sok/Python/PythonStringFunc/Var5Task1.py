def line_e(x):
    if len(x) != 5 or x[1] not in "+-" or x[3] != "=":
        print("Error: incorrect input")
        return None
    else:
        if x[0] == "x":
            return int(x[4]) - int(x[2]) if x[1] == "+" else int(x[4]) + int(x[2])
        elif x[2] == 'x':
            return int(x[4]) - int(x[0]) if x[1] == "+" else int(x[0]) - int(x[4])
        else:
            return int(x[0]) + int(x[2]) if x[1] == "+" else int(x[0]) - int(x[2])



with open('INPUT_task1.txt', 'r') as f:
    equation = f.read().strip()

result = line_e(equation)

with open('OUTPUT_task1.txt', 'w') as f:
    f.write(str(result))