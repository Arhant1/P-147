from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background="light blue")

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text="Name of Ascii : ", bg= "light yellow", fg="black")
label2 = Label(root, text="Encrypted name : ", bg= "snow", fg="black")
def asciiConverter():
    hey = enter_word.get()
    
    for letter in hey:
        label["text"] += str(ord(letter)) + " "
        
def encrypted():
    label = ascci
    ascci = int(ord(letter))
    encrypted = ascci - 1
    
    for letter in ascii:
        label2["text"] += str(chr(encrypted))

btn=Button(root, text="Display the Ascii Code and Encrypted value", command=asciiConverter, bg='blue', fg='snow')
btn.place(relx=0.5,rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)
label2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()

