#hello, this app I creat, decause I`m was boring. So this app-the joke. Button No, change position, so user can
#tap only button yes

from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox



root = Tk()

# Here you can insert your photo, and it will appear in the last window.
#root.iconphoto(True, tk.PhotoImage(file=' '))



root.title("Оценочка.")
root.geometry("500x200")

text = Label(root, text="Добрый день, \nпоставите хорошую оценку?")
text.place(x = 80, y = 0)
text.config(font=("Courier",25))

def buttonCallback():
    messagebox.showinfo("Спасибо", "Спасибо!\n Создатель M_B_PRESS_F.)")


button1=tk.Button(root, text="Да", height = 3, width = 5, command=buttonCallback)
button1.place(x=100, y=100)
button1.config(font=("Courier",15))


x1, y1  = 340, 100

def new_button():
    global button2
    button2=tk.Button(root, text="Нет", height = 3, width = 5, command= new_button1)
    button2.config(font=("Courier",15))
    button2.place(x = x1, y = y1)


    

def new_button1():
    global button3
    button2.destroy()    
    button3=tk.Button(root, text="Нет", height = 3, width = 5, command=new_button2)
    button3.config(font=("Courier",15))
    random_place_button1 = random.randint(0,470)
    random_place_button2 = random.randint(0,170)
    button3.place(x = random_place_button1, y = random_place_button2)



def new_button2():
    global button3
    button3.destroy()
    button3 = tk.Button(root, text="Нет", height = 3, width = 5,command= new_button2)

    random_place_button1 = random.randint(0,470)
    random_place_button2 = random.randint(0,150)
    button3.place(x = random_place_button1, y = random_place_button2)
    
    button3.config(font=('Courier', 15))

new_button()

if __name__ == "__main__":
    root.mainloop()





















