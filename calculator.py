from tkinter import*


def additon():
    x = int(first.get())
    y = int(second.get())
    a1=( x+y)
    print (a1)


def subtraction():
    x = int(first.get())
    y = int(second.get())
    a1=( x-y)
    print (a1)

def multiplication():
    x = int(first.get())
    y = int(second.get())
    a1=( x*y)
    print (a1)

def division():
    x = int(first.get())
    y = int(second.get())
    a1=( x/y)
    print (a1)


root=Tk()
root.title("CALCULATOR")
root.minsize(height=400,width=400)
heading_label= Label(root,text="CALCULATOR")
heading_label.config(font=("TIMES NEW ROMAN",20,'bold'))
heading_label.grid(sticky='e',pady=55)
heading_lable2=Label(root,text="ENTER THE FIRST NUMBER",font=("TIMES NEW ROMAN",16,'bold'))
heading_lable2.grid(row=1,column=0)
entry=Entry(root)
first=entry
entry.grid(row=1,column=5,sticky='e')
heading_label3=Label(root,text="ENTER THE SECOND NUMBER",font=("TIMES NEW ROMAN",16,'bold'))
heading_label3.grid(row=2,column=0)
entry2=Entry(root)
second=entry2
entry2.grid(row=2,column=5,sticky='e')
button=Button(root,text="+",command=additon,font=(45))
button.grid(row=9,column=0,pady=45,padx=41)
button1=Button(root,text="-",command=subtraction,font=(45))
button1.grid(row=9,column=45,padx=20)
button2=Button(root,text="*",command=multiplication,font=45)
button2.grid(row=9,column=3,padx=59)
button3=Button(root,text="/",command=division,font=(45))
button3.grid(row=9,column=2,padx=29)

root.mainloop()
