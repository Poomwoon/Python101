from tkinter import *
from tkinter import ttk #them of tk
from tkinter import messagebox

GUI = Tk() # หน้าจอหลัก
GUI.title('โปรแกรมคำนวณราคาทอง') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม

L1 = Label(GUI,text='คำนวณราคาทอง',font=('Angsana New',30),fg='Red')
L1.place(x=150,y=10)

L2 = Label(GUI,text='ราคาทองวันนี้บาทละ 29,650 บาท',font=('Angsana New',15),fg='Green')
L2.place(x=50,y=100)

L3 = Label(GUI,text='ราคาทองต่อกรัม',font=('Angsana New',15),fg='Green')
L3.place(x=50,y=180)

##################

def Button2():
    text = 'ทองคำวันนี้ราคากรัมละ 1,955 บาท'
    messagebox.showinfo('คำนวณ',text)

FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=200,y=160)
B2 = ttk.Button(FB1,text='คำนวณ',command=Button2)
B2.pack(ipadx=30,ipady=20)



GUI.mainloop()
