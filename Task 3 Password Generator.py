import random
from tkinter import*


window=Tk()
window.geometry("300x300")
window.config(background="skyblue")

passlen=IntVar()
passStr=StringVar()
passlen.set(0)

def pwdG():
    
    characters ="qwertyuioplkjhgfdsazxcvbnm1234567890!@#$%^&*+=_-/?:;"

    password = ""   

    for i in range(passlen.get()):
        password = password + random.choice(characters)

    passStr.set(password)
    
Label(window, text="_________________PASSWORD GENERATOR_________________",bg="skyblue").pack()


Label(window, text="Enter password length", bg="skyblue").pack(pady=3,padx=3)


Entry(window, textvariable=passlen, fg="black").pack(pady=3)


Button(window, text="Generate Password", command=pwdG, fg="skyblue", bg="black").pack(pady=7)


Entry(window, textvariable=passStr).pack(pady=3)


window.mainloop()

