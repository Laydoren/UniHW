import tkinter as tk
import json

current_question = 0
count_c = 0
count_un = 0

file = open("test.txt", "r", encoding="utf-8")
data = json.load(file)
file.close()

def show_question():
    global current_question
    q = data["questions"][current_question]
    question_label.config(text=f"Вопрос {current_question + 1}: {q['question']}")

    for i, option_text in enumerate(q["answers"]):
        check_vars[i].set(0)
        check_buttons[i].config(text=f"{i + 1}. {option_text}")
        check_buttons[i].pack(anchor="w", padx=100)

    check_feedback.config(text="")

def check_question():
    global current_question, count_c, count_un
    q_list = data["questions"]
    correct_indices = q_list[current_question]["correct"]

    user_choices = [i for i, var in enumerate(check_vars) if var.get() == 1]

    if not user_choices:
        check_feedback.config(text="Выберите вариант!", fg="orange")
        return

    if sorted(user_choices) == sorted(correct_indices):
        check_feedback.config(text="Правильно!", fg="green")
        count_c += 1
    else:
        check_feedback.config(text="Неправильно!", fg="red")
        count_un += 1

    if current_question < len(q_list) - 1:
        baseWindow.after(1000, next_question)
    else:
        baseWindow.after(1000, end_test)

def next_question():
    global current_question
    current_question += 1
    show_question()

def end_test():
    total = count_c + count_un
    percent = round((count_c / total) * 100, 1)

    question_label.config(
        text=f"Тест завершён!\n"
             f"Правильных: {count_c}\n"
             f"Неправильных: {count_un}\n"
             f"Результат: {percent}%"
    )

    if percent >= 90:
        mark, color = "5", "green"
    elif percent >= 70:
        mark, color = "4", "blue"
    elif percent >= 40:
        mark, color = "3", "orange"
    else:
        mark, color = "2", "red"

    estimation.config(text=f"Оценка: {mark}", fg=color)

    for cb in check_buttons:
        cb.pack_forget()
    click_button.pack_forget()
    check_feedback.pack_forget()


baseWindow = tk.Tk()
baseWindow.title("Тестирование: Доктор Кто")
baseWindow.geometry("1000x600")

question_label = tk.Label(baseWindow, text="", font="Arial 18", wraplength=800)
question_label.pack(pady=40)

check_vars = [tk.IntVar() for _ in range(4)]
check_buttons = []
for i in range(4):
    cb = tk.Checkbutton(baseWindow, text="", variable=check_vars[i], font="Arial 14")
    check_buttons.append(cb)

click_button = tk.Button(baseWindow, text="Ответить", command=check_question, font="Arial 14")
click_button.pack(pady=20)

check_feedback = tk.Label(baseWindow, text="")
check_feedback.pack()

estimation = tk.Label(baseWindow, text="", font="Arial 16 bold")
estimation.pack()

show_question()
baseWindow.mainloop()