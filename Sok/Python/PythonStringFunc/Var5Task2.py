def words_lecture(n, m, text):
    words = set([text[i:i + m] for i in range(n - m + 1)])
    return len(words)


with open('INPUT_task2.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    num = f.readline().strip()

result = words_lecture(n, m, num)

with open('OUTPUT_task2.txt', 'w') as f:
    f.write(str(result))