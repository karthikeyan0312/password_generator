from tkinter import *
import random
def passwd():
    #passlen = int(input("enter the length of password"))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p = "".join(random.sample(s,20))
    text.delete(1.0,'end')
    text.insert(1.0,p)
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('500x300')

text = Text(root, height=5,width=30)
# Create a Button
btn = Button(root, text = 'generate password', bd = '5',command = passwd)
 
# Set the position of button on the top of window.  
btn.place(x=195,y=170)
text.pack()
root.mainloop()