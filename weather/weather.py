from tkinter import *
import requests
from tkinter import messagebox
import time

API_KEY = "4046d6a20a41ff3b66f8c9e5ecc934bb"
API_URL = f"https://api.openweathermap.org/data/2.5/weather"


def print_weather(weather):
    try:
        city = weather["name"]
        country = weather["sys"]["country"]
        temp = weather["main"]["temp"]
        press = weather["main"]["pressure"]
        humidity = weather["main"]["humidity"]
        wind = weather["wind"]["speed"]
        desc = weather["weather"][0]["description"]
        sunrise_ts = weather["sys"]["sunrise"]
        sunset_ts = weather["sys"]["sunset"]
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime("%H : %M : %S", sunrise_struct_time)
        sunset = time.strftime("%H : %M : %S", sunset_struct_time)
        return f"Местоположение: {city}, {country} \nТемпература: {temp} *С \nАтм. давление: {press} гПа\nВлажность: {humidity}% \nСкорость ветра: {wind} м\с\n" \
               f"Погодные условия: {desc} \nВосход: {sunrise} \nЗакат: {sunset}"
    except:
        return "Ошибка преобразования данных"


def get_weather(event=''):
    if not entry_weather.get():
        messagebox.showerror(title="Ошибка", message="Введите город")
    else:
        params = {
            "appid": API_KEY,
            "q": entry_weather.get(),
            "units": "metric",
            "lang": "ru"
        }

        resp = requests.get(API_URL, params=params)
        data_weather = resp.json()

        if data_weather["cod"] == "404":
            text_result.delete('1.0', END)
            text_result.insert('1.0', f"Ошибка получения данных \n{data_weather['message']}")
        else:
            text_result.delete('1.0', END)
            text_result.insert('1.0', print_weather(data_weather))


def clear_entry_weather(event=''):
    entry_weather.delete(0, END)


root = Tk()
root.geometry("400x300")
root.title("Weather")
# root.resizable(0, 0)


top_frame = Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor=N)

entry_weather = Entry(top_frame)
entry_weather.place(relwidth=0.7, relheight=1)
entry_weather.insert(0, "Enter city")
entry_weather.bind("<Button-1>", clear_entry_weather)

button = Button(top_frame, text="Запрос погоды", command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor=N)

text_result = Text(lower_frame)
text_result.pack()

entry_weather.bind("<Return>", get_weather)

root.mainloop()
