import tkinter
from tkinter import*
root=tkinter.Tk()
root.title("WELCOME")
# root.geometry("600x600")
label=tkinter.Label(root,text="TEAM PROJECT",font=("arial",50),padx=10,pady=10)
label.pack()
# def clicked():
#     label=tkinter.Lable(root,text="window",font=("arial",30))
#     label.pack(pady=10)
my_listbox=Listbox(root)
my_listbox.pack(pady=15)
my_listbox.insert(END,"these are languages")
my_listbox.insert(END,"progamming language")
my_list=["python","css","html","sql"]
for i in my_list:
    my_listbox.insert(0,i)
def delete():
    my_listbox.delete(tkinter.END)
    # my_label.config(text=my_listbox.get(ANCHOR))
# def add():
#     my_listbox.add(ANCHOR)
    # my_label.config(text=my_listbox.get(ANCHOR))
def add():
    # task=entry_task.get()
    my_listbox.insert(tkinter.END)
b=Button(root,text="Delete",padx=20,pady=20,bg="black",fg="white",font=("arial",20),command=delete)
b.pack(padx=50,pady=30,side="right")
b=Button(root,text="Add",padx=20,pady=20,bg="black",fg="white",font=("arial",20),command=add)
b.pack(padx=50,pady=30,side="right")
global my_label
my_label=Label(root,text="")
my_label.pack(padx=10,pady=10)
t=Entry(root,width=20,font=40)
t.pack(padx=10,pady=50)
root.mainloop()



# import tkinter
# import tkinter. messagebox
# from turtle import width
# root=tkinter.Tk()
# root.title("Team Project")
# def add_task():
#     task=entry_task.get()
#     listbox_task.insert(tkinter.END,task)
# listbox_task=tkinter.Listbox(root,height=3,width=50)
# listbox_task.pack()
# entry_task=tkinter.Entry(root,width=50)
# entry_task.pack()
# button_add_task=tkinter.Button(root,text="add element",width=48,command=add_task)
# button_add_task.pack()
# root.mainloop()