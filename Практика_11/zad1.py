import requests
from tkinter import *


APPID = '8292f3dddd09300935af82bdf6481fe6'
city = "Санкт-Петербург"
URL = "http://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": APPID,
    "units": "metric",
    "lang": "ru"
}


response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Погода в городе {data['name']} ({data['sys']['country']}):")
    print(f"Температура: {data['main']['temp']}°C")
    print(f"Ощущается как: {data['main']['feels_like']}°C")
    print(f"Погодные условия: {data['weather'][0]['description']}")
    print(f"Ветер: {data['wind']['speed']} м/с")
    print(f"Видимость: {data['visibility'] / 100}%")
else:
    print(f"Ошибка {response.status_code}: {response.text}")


def our_loc():
    params = {
        "q": "Санкт-Петербург",
        "appid": APPID,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    output.config(text=f"Погода в городе {data['name']} ({data['sys']['country']}):\nТемпература: {data['main']['temp']}°C\n"
                       f"Ощущается как: {data['main']['feels_like']}°C\nПогодные условия: {data['weather'][0]['description']}\n"
                       f"Ветер: {data['wind']['speed']} м/с\nВидимость: {data['visibility'] / 100}%")


def moscow():
    params = {
        "q": "Москва",
        "appid": APPID,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    output.config(text=f"Погода в городе {data['name']} ({data['sys']['country']}):\nТемпература: {data['main']['temp']}°C\n"
                       f"Ощущается как: {data['main']['feels_like']}°C\nПогодные условия: {data['weather'][0]['description']}\n"
                       f"Ветер: {data['wind']['speed']} м/с\nВидимость: {data['visibility'] / 100}%")


def tokyo():
    params = {
        "q": "Токио",
        "appid": APPID,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    output.config(text=f"Погода в городе {data['name']} ({data['sys']['country']}):\nТемпература: {data['main']['temp']}°C\n"
                       f"Ощущается как: {data['main']['feels_like']}°C\nПогодные условия: {data['weather'][0]['description']}\n"
                       f"Ветер: {data['wind']['speed']} м/с\nВидимость: {data['visibility'] / 100}%")


def by_name():
    params = {
        "q": entry1.get(),
        "appid": APPID,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    output.config(text=f"Погода в городе {data['name']} ({data['sys']['country']}):\nТемпература: {data['main']['temp']}°C\n"
                       f"Ощущается как: {data['main']['feels_like']}°C\nПогодные условия: {data['weather'][0]['description']}\n"
                       f"Ветер: {data['wind']['speed']} м/с\nВидимость: {data['visibility'] / 100}%")


def by_coords(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": APPID,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    output.config(
        text=f"Погода по координатам {data['coord']['lat']}, {data['coord']['lon']} ({data['sys']['country']}):\nТемпература: {data['main']['temp']}°C\n"
             f"Ощущается как: {data['main']['feels_like']}°C\nПогодные условия: {data['weather'][0]['description']}\n"
             f"Ветер: {data['wind']['speed']} м/с\nВидимость: {data['visibility'] / 100}%")


root = Tk()
root.title('Погода')
root.geometry('750x500')
btn = Button(root, text='Санкт-Петербург', command=our_loc)
btn.pack()
btn2 = Button(root, text='Москва', command=moscow)
btn2.pack()
btn3 = Button(root, text='Токио', command=tokyo)
btn3.pack()
btn4 = Button(root, text='Узнать по координатам', command=lambda: by_coords(entry1.get(), entry2.get()))
btn4.pack()
btn5 = Button(root, text='Узнать по названию', command=by_name)
btn5.pack()
entry1 = Entry()
entry1.pack(anchor=N)
entry2 = Entry()
entry2.pack(anchor=S)
output = Label(root)
output.pack(side=TOP)
root.mainloop()