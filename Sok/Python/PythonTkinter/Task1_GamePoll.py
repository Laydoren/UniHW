import tkinter as tk
import json
import os

def clickButton():
    if not os.path.exists("games_results.txt"):
        with open("games_results.txt", "w", encoding="utf-8") as file:
            file.write("")

    with open("games_results.txt", "r", encoding="utf-8") as file:
        content = file.read()

    if content.strip() == "":
        data_users = dict()
    else:
        try:
            data_users = json.loads(content)
        except json.JSONDecodeError:
            data_users = dict()

    user = userName.get()
    change_1 = radio_value.get()
    change_2 = radio_value2.get()
    change_3 = radio_value3.get()

    data_questionnaire = dict()

    q1_text = question1.cget("text")
    data_questionnaire[q1_text] = []
    genres = {1: "RPG", 2: "Шутеры", 3: "Стратегии", 4: "Хорроры", 5: "Спортивные симуляторы"}
    data_questionnaire[q1_text].append(genres.get(change_1, "Не выбрано"))

    q2_text = question2.cget("text")
    data_questionnaire[q2_text] = []
    platforms = {1: "ПК (PC)", 2: "Игровая консоль (PlayStation/Xbox/Switch)", 3: "Мобильный телефон", 4: "Облачный гейминг"}
    data_questionnaire[q2_text].append(platforms.get(change_2, "Не выбрано"))

    q3_text = question3.cget("text")
    data_questionnaire[q3_text] = []
    priorities = {1: "Сюжет и лор", 2: "Геймплей и механики", 3: "Графика и визуал", 4: "Мультиплеер и общение"}
    data_questionnaire[q3_text].append(priorities.get(change_3, "Не выбрано"))

    if user.strip() == "":
        user = "Аноним"

    if user not in data_users:
        data_users[user] = []

    data_users[user].append(data_questionnaire)

    with open("games_results.txt", "w", encoding="utf-8") as file:
        json.dump(data_users, file, ensure_ascii=False, indent=4)


baseWindow = tk.Tk()
baseWindow.title("Игровая Анкета")
baseWindow.geometry("1000x950")

heading = tk.Label(baseWindow, text="Анкета: Видеоигры", fg="blue", font="Arial 18 bold")
heading.pack(pady=10)

name = tk.Label(baseWindow, text="Введите ваш никнейм или имя:", fg="#1a5276", font="Arial 14")
name.pack()

userName = tk.Entry(baseWindow, width=40, font="Arial 12")
userName.pack(pady=5)


frame1 = tk.LabelFrame(baseWindow, text="Предпочтения", fg="#1a5276", font="Arial 12 bold", pady=10)
frame1.pack(fill="x", padx=100, pady=10)

radio_value = tk.IntVar()
question1 = tk.Label(frame1, text="Какой жанр игр вам ближе всего?", fg="black", font="Arial 13")
question1.pack()

genres_list = [("RPG", 1), ("Шутеры", 2), ("Стратегии", 3), ("Хорроры", 4), ("Спортивные симуляторы", 5)]
for text, val in genres_list:
    tk.Radiobutton(frame1, text=text, font="Arial 12", value=val, variable=radio_value).pack(anchor="w", padx=20)


frame2 = tk.LabelFrame(baseWindow, text="Платформа", fg="#1a5276", font="Arial 12 bold", pady=10)
frame2.pack(fill="x", padx=100, pady=10)

radio_value2 = tk.IntVar()
question2 = tk.Label(frame2, text="На чем вы чаще всего играете?", fg="black", font="Arial 13")
question2.pack()

platforms_list = [("ПК (PC)", 1), ("Консоль", 2), ("Смартфон", 3), ("Облачные сервисы", 4)]
for text, val in platforms_list:
    tk.Radiobutton(frame2, text=text, font="Arial 12", value=val, variable=radio_value2).pack(anchor="w", padx=20)


frame3 = tk.LabelFrame(baseWindow, text="Важные аспекты", fg="#1a5276", font="Arial 12 bold", pady=10)
frame3.pack(fill="x", padx=100, pady=10)

radio_value3 = tk.IntVar()
question3 = tk.Label(frame3, text="Что для вас важнее всего в игре?", fg="black", font="Arial 13")
question3.pack()

aspects_list = [("Сюжет и лор", 1), ("Геймплей и механики", 2), ("Графика и визуал", 3), ("Мультиплеер", 4)]
for text, val in aspects_list:
    tk.Radiobutton(frame3, text=text, font="Arial 12", value=val, variable=radio_value3).pack(anchor="w", padx=20)


click = tk.Button(baseWindow, text="Сохранить ответы", fg="white", bg="green", font="Arial 16 bold", command=clickButton)
click.pack(pady=20)

baseWindow.mainloop()
