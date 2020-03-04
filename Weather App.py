import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import requests
import string


cHeight = 410
cWidth = 700



def on_entry_click(event):
    if entry.get() == 'zip code':
       entry.delete(0, "end") 
       entry.insert(0, '') 
       entry.config(fg = 'black')
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'zip code')
        entry.config(fg = 'grey')

def information(weather):
    try:
        name = (weather['name'])
        description = (weather['weather'][0]['description'])
        temperature = (weather['main']['temp'])
        humidity = (weather['main']['humidity']) 

        results = 'City: %s \nClouds: %s \nTemperature (°C): %s \nHumidity: %s' % (name, description, temperature, (str(humidity)+"%"))
    except: 
	    results = 'Invalid Zip code'

    return results

def get_weather(zipcode):
        readApikey = open("apikey.gitignore", "r")
        weather_key = readApikey.read()
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'appid': weather_key, 'zip': zipcode, 'units': 'metric'}
        response = requests.get(url, params=params)
        weather = response.json()
        
        label['text'] = information(weather)
        readApikey.close()
        
        



root = tk.Tk()
root.title('Weather App')
root.iconphoto(False, tk.PhotoImage(file='icon.png'))



canvas = tk.Canvas(root, height=cHeight, width=cWidth, bd=20)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open("background.png"))  
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="green", bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=0.7, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=16)
entry.bind("<Return>", (lambda event: get_weather(entry.get())))
entry.place (relheight=1, relwidth=0.7)
entry.insert(0, 'zip code')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.config(fg = 'grey')



button = tk.Button(frame, text="Weather", font=16, command=lambda: get_weather(entry.get()))
button.place(relx=.75, relheight=1, relwidth=0.25)

lower_frame = tk.Frame(root, bg="blue", bd=5)
lower_frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.7, anchor="n")


label = tk.Label(lower_frame, font=('Helvetica', 30))
label.place(relwidth=1, relheight=1)



root.mainloop()

