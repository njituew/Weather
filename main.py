import requests
from tkinter import *
from tkinter.messagebox import showerror


def click():
    if input_field.get() != '':
        try:
            # last city
            global last_city
            global n
            if n < 2: n += 1
            if n == 2:
                last_city_button.place(x=0, y=170)
            last_city_button.configure(text=last_city)
            last_city = input_field.get().title()
            # processing the current request
            city = input_field.get().title()
            weather_data = requests.get(url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+
                                              '&units=metric&lang=eng&appid=2b328558758776732bb4ebe9fc2b431f').json()
            weather_result = f"{weather_data['name']}: {round(weather_data['main']['temp'])}°C (feels like {round(weather_data['main']['feels_like'])}°C), " \
                             f" {weather_data['weather'][0]['description'].lower()}," \
                             f" wind {round(weather_data['wind']['speed'], 1)}m/s."
            result_label.configure(text=weather_result)
        except:
            showerror(title='Error', message='Not found')

def click_last_place():
    weather_data = requests.get(url='https://api.openweathermap.org/data/2.5/weather?q=' + last_city_button['text'] +
                                    '&units=metric&lang=eng&appid=2b328558758776732bb4ebe9fc2b431f').json()
    weather_result = f"{weather_data['name']}: {round(weather_data['main']['temp'])}°C (feels like {round(weather_data['main']['feels_like'])}°C), " \
                     f" {weather_data['weather'][0]['description'].lower()}, wind {round(weather_data['wind']['speed'], 1)}m/s."
    result_label.configure(text=weather_result)
    input_field.delete(0, END)


# window
root = Tk()
w = 500
h = 200
root.geometry(f"{w}x{h}+{(root.winfo_screenwidth()-w)//2}+{(root.winfo_screenheight()-h)//2}")
root.resizable(0, 0)
root.title('Weather.py')
bg_color = '#63707A'
fg_color = '#11C1AE'
root.configure(bg=bg_color)
root.grid_columnconfigure(0, weight=1)

# variables
last_city = ''
n = 0   # the variable n is a counter, thanks to which the last_city_button appears at the right moment

# top label
top_label = Label(root, text='Type your city:', font='Bahnschrift 14', bg=bg_color, fg=fg_color)
top_label.grid(column=0, row=0, pady='14')

# input field
input_field = Entry(root, font='Bahnschrift 14', bg=bg_color, fg=fg_color, justify=CENTER)
input_field.grid(column=0, row=1)

# search button
search_image = PhotoImage(file='search.png').subsample(16, 16)
search_button = Button(root, image=search_image, bg=bg_color, command=click)
search_button.place(x=353, y=57)

# result label
result_label = Label(root, text='', font='Bahnschrift 12', bg=bg_color, fg=fg_color)
result_label.grid(column=0, row=3, pady='14')

# weather icon
weather_icon = PhotoImage(file='weather icon.png').subsample(6, 6)
Label(root, image=weather_icon, bg=bg_color).place(x=0, y=0)

# last city button$
Label(root, text='Last city:', font='Bahnschrift 10', bg=bg_color, fg=fg_color).place(x=0, y=140)
last_city_button = Button(root, text='', font='Bahnschrift 10', bg=bg_color, fg=fg_color,
                          command=click_last_place)

root.mainloop()
