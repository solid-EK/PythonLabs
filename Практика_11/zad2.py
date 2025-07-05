import requests
from tkinter import *
response = requests.get('https://official-joke-api.appspot.com/random_joke')
data = response.json()
print(f"Случайная шутка:\n{data['setup']}\n{data['punchline']}")


def joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = response.json()
    out.config(text=f"Случайная шутка:\n{data['setup']}\n{data['punchline']}\nПорядковый № шутки: {data['id']}")


root = Tk()
root.title('Случайная шутка')
root.geometry('500x200')
btn = Button(root, text='Посмеятся', command=joke)
btn.pack()
out = Label(root)
out.pack()
root.mainloop()