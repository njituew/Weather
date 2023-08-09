import requests
from tkinter import *
from tkinter.messagebox import showerror


def click():
    try:
        city = input_field.get().title()
        weather_data = requests.get(url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+
                                          '&units=metric&lang=eng&appid=2b328558758776732bb4ebe9fc2b431f').json()
        weather_result = f"{weather_data['name']}: {round(weather_data['main']['temp'])}°C (feels like {round(weather_data['main']['feels_like'])}°C), " \
                         f" {weather_data['weather'][0]['description'].lower()}, wind {round(weather_data['wind']['speed'], 1)}m/s."
        result_label.configure(text=weather_result)
    except:
        showerror(title='Error', message='Not found')


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

# top label
top_label = Label(root, text='Type your city:', font='Bahnschrift 14', bg=bg_color, fg=fg_color)
top_label.grid(column=0, row=0, pady='14')

# input field
input_field = Entry(root, font='Bahnschrift 10', bg=bg_color, fg=fg_color, justify=CENTER)
input_field.grid(column=0, row=1)

# search button
search_image = PhotoImage(file='search.png').subsample(20,20)
search_button = Button(root, image=search_image, bg=bg_color, command=click)
search_button.place(x=324, y=55)

# result label
result_label = Label(root, text='', font='Bahnschrift 12', bg=bg_color, fg=fg_color)
result_label.grid(column=0, row=3, pady='14')

# weather icon
weather_icon = PhotoImage(file='weather icon.png').subsample(6, 6)
Label(root, image=weather_icon, bg=bg_color).place(x=0, y=0)

root.mainloop()