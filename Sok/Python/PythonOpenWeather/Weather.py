import requests

API_KEY = "d3fec7e37ab0749f474c6c3e4ce41f89"

city = input("Введите город: ")

try:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(data)
        print(f"\nПогода в {data['name']}:")
        print(f"Температура: {data['main']['temp']}°C")
        print(f"Ощущается как: {data['main']['feels_like']}°C")
        print(f"Погода: {data['weather'][0]['description']}")
        print(f"Влажность: {data['main']['humidity']}%")
        print(f"Давление: {data['main']['pressure']} hPa")
        print(f"Ветер: {data['wind']['speed']} м/с")
    else:
        print(f"Ошибка: {data['message']}")

except Exception as e:
    print(f"Произошла ошибка: {e}")
