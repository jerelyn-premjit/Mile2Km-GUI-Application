from tkinter import *

window = Tk()
def clicked():
  n = float(input.get())
  kilo = n*1.60934
  l3["text"]=kilo

window.minsize(width=100,height=100)
window.title("Mile2Km")
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

l1 = Label(text = "Miles")
l1.grid(column=2, row=0)

l2 = Label(text = "is equal to")
l2.grid(column=0, row=1)

l3= Label(text = "0")
l3.grid(column=1, row=1)

l4= Label(text = "km")
l4.grid(column=2, row=1)

but = Button(text="calculate",command=clicked)
but.grid(column=1,row=2)

window.config(padx=20,pady=20)


window.mainloop()