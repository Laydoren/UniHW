import requests
from datetime import datetime

API_KEY = "d3fec7e37ab0749f474c6c3e4ce41f89"

print("Прогноз погоды, или нет, просто погода в данный момент времени и пространства")
print("Введите 'выход' для завершения работы.")

while True:
    city = input("\nВведите город: ").strip()

    if city.lower() == 'выход':
        print("Завершение работы. Хорошего дня!")
        break

    if not city:
        continue

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            name = data['name']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind_speed = data['wind']['speed']
            clouds = data['clouds']['all']

            sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
            sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

            print(f"\nПогода в {name}:")
            print(f"  Температура: {temp}°C (ощущается как {feels_like}°C)")
            print(f"  Описание: {desc.capitalize()}")
            print(f"  Влажность: {humidity}%")
            print(f"  Давление: {pressure} hPa")
            print(f"  Ветер: {wind_speed} м/с")
            print(f"  Облачность: {clouds}%")
            print(f"  Восход: {sunrise}")
            print(f"  Закат: {sunset}")
        else:
            print(f"Ошибка: {data.get('message', 'Город не найден')}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
